### Twitter Sentiment Search

This simple flask application takes a query and then returns five tweets labelled according to their sentiment (positive or negative). You can increase the number of tweets returned by adjusting the `search_twitter()` method, but it is currently set at 5 due to rate limiting.

This app is not hardened for production and should be considered more of a proof of concept or experiment.

### Installation

Some dependencies are not included in this repository. To install them run `python install.py`. The script will install the python 2.7 dependencies, download the Twitter sentiment analysis repository, download and rename the Twitter sentiment dataset and then run the sentiment analysis algorithm to create python pickles that are used in the Flask application to provide prediction for searched tweets.

### Running

You will need twitter oAuth tokens to run the application. See line 16 in `appy.py`. I may get around to creating a proper config file if I ever harden the application for production.

Once configuration is complete, run `python app.py`.

### License

Copyright (c) 2016 Michael Raypold

See LICENSE
