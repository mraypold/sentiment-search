### Twitter Sentiment Search

This simple flask application takes a query and then returns five tweets labelled according to their sentiment (positive or negative). You can increase the number of tweets returned by adjusting the `search_twitter()` method, but it is currently set at 5 due to rate limiting.

This app is not hardened for production and should be considered more of a proof of concept or experiment.

### Installation

`pip install -r requirements.txt`

`python install.py` This will install the sentiment analysis repo and create the python pickles used in the flask application.

### Running

You will need twitter oAuth tokens to run the application. See line 16 in `appy.py`. I may get around to creating a proper config file if I ever harden the application for production.

Once configuration is complete, run `python app.py`.

### License

Copyright (c) 2016 Michael Raypold

See LICENSE
