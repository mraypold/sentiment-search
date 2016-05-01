from flask import Flask, request

import re
import json

import pandas as pd
import numpy as np
from sklearn.externals import joblib

from twitter import *

app = Flask(__name__, static_url_path='')
app.debug = False

# TODO move this into a config class
t = Twitter(auth=OAuth(
                        'token',
                        'token-key',
                        'con-secret',
                        'con-secret-key'))

# Load the necessary SA classifiers
print 'Loading vectorizer and classifier from pickles.'
print 'This will take a couple seconds...'
vectorizer = joblib.load('./twitter-sentiment/vectorizer.pkl')
classifier = joblib.load('./twitter-sentiment/classifier.pkl')
print 'Loading done!'

def predict(text):
    '''Takes a string of text and returns whether True for positive sentiment'''
    x = vectorizer.transform([text])
    return bool(classifier.predict(x)[0])

# Some utils to clean up 'dirty' tweets that will throw off the SA algorithm

def remove_links(tweet):
    '''Takes a tweet and removes the links in the text'''
    return re.sub(r'(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', '', tweet)

def remove_names(tweet):
    '''Takes a tweet and removes the usernames and @ symbol'''
    return re.sub(r'\@\w+', '', tweet)

# see https://dev.twitter.com/rest/reference/get/search/tweets
def search_twitter(lookup):
    '''Takes a lookup term and returns twitter search results'''
    return t.search.tweets(q = lookup, lang = 'en', result_type='popular', count=5)

@app.route('/')
def hello_world():
    return app.send_static_file('index.html')

@app.route('/tweets')
def get_tweets():
    term = request.args.get('search')
    results = search_twitter(term)

    statuses = results['statuses']

    sentiments = []

    for status in statuses:
        cleaned = remove_links(status['text'])
        cleaned = remove_names(cleaned)
        pos_sentiment = predict(cleaned)

        res = {
            'id': status['id_str'],
            'positive': pos_sentiment
        }
        sentiments.append(res)

    return json.dumps(sentiments)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
