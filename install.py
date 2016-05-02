#
# Installs all the required dependencies for the flask application.
#

import os
import requests
import zipfile
import StringIO
from git import Repo

# Pull the sentiment analysis repository.
repo_url = 'https://github.com/mraypold/twitter-sentiment.git'
Repo.clone_from(repo_url, 'twitter-sentiment')

# Download the sentiment analysis dataset.
# Unzip the dataset
# Rename the dataset
zip_file_url = 'http://thinknook.com/wp-content/uploads/2012/09/Sentiment-Analysis-Dataset.zip'
r = requests.get(zip_file_url, stream=True)
z = zipfile.ZipFile(StringIO.StringIO(r.content))
z.extractall('twitter-sentiment')
os.rename('./twitter-sentiment/Sentiment Analysis Dataset.csv', './twitter-sentiment/Sentiment_Analysis_Dataset.csv')

# Run the sentiment analysis program.
# Change directory so that sentiment.py does not look for the dataset
# in the current directory.
os.chdir('./twitter-sentiment')
os.system('python sentiment.py')
