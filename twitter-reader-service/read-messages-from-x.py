import tweepy
import os
import requests
import logging


# Set up Twitter API credentials
logging.info("Setting up Twitter API credentials...")
API_KEY = os.getenv('TWITTER_API_KEY')
API_SECRET_KEY = os.getenv('TWITTER_API_SECRET_KEY')
ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')

# Send tweets to the REST API
api_url = "http://api_service:5000/predict"

# Authenticate to Twitter API
logging.info("Authenticating to Twitter API...")
client = tweepy.Client(bearer_token=BEARER_TOKEN)

def search_tweets(query, max_results=100):
    try:
        # response = {"Review": "This are mysteriously bad. Unknown everywhere"}
        # requests.post(api_url, json=response["Review"])
        
        # Search for tweets matching the query
        logging.info(f"Searching for tweets with query: {query}")
        response = client.search_recent_tweets(
            query=query,
            max_results=max_results,
            tweet_fields=["lang"]
        )

        if response.data:
            for tweet in response.data:
                if tweet.lang == 'en':  # Check if the tweet is in English
                    tweet = {
                        "Review": tweet.text,
                        "lang": tweet.lang
                    }
                    # Send the tweet to the REST API for prediction
                    logging.info("Sending tweet to API...")
                    response = requests.post(api_url, json=tweet["Review"])
                    logging.info("Response from API:", response.json())
        else:
            return "No tweets found."

    except tweepy.TooManyRequests as e:
        logging.info(f"Error: {e}")
        logging.info("Rate limit exceeded. Wait for reset.")

# tweets_data = search_tweets('US Elections')
# print(tweets_data)