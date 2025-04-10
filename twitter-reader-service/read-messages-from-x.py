# Description: This script reads tweets from X/Twitter using the X/Twitter API and sends them to API for further processing.
# Authenticates to X API using credentials
# Searches for tweets based on a query
# Filters tweets (only English tweets)
# Sends tweets to the API (/predict endpoint) for sentiment analysis

# Import libraries
import tweepy
import os
import requests
import logging


# Set up Twitter API credentials - credential management
# Use environment variables to store sensitive information
logging.info("Setting up Twitter API credentials...")
API_KEY = os.getenv('TWITTER_API_KEY')
API_SECRET_KEY = os.getenv('TWITTER_API_SECRET_KEY')
ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')

# Send tweets to the REST API
api_url = "http://api_service:5000/predict"

# Authenticate to Twitter API
# Uses tweepy library for Twitter API interaction
# Note: The bearer token is used for authentication in the Twitter API v2
logging.info("Authenticating to Twitter API...")
client = tweepy.Client(bearer_token=BEARER_TOKEN)

def search_tweets(query, max_results=100):
    try:
        # response = {"Review": "This are mysteriously bad. Unknown everywhere"}
        # requests.post(api_url, json=response["Review"])
        
        # Search for tweets matching the query
        logging.info(f"Searching for tweets with query: {query}")
        
        # Search recent tweets using the Twitter API
        # Note: The max_results parameter is limited to 100 by Twitter API
        response = client.search_recent_tweets(
            query=query,
            max_results=max_results,
            tweet_fields=["lang"]
        )

        if response.data: # Check if there are any tweets in the response
            for tweet in response.data:
                if tweet.lang == 'en':  # Check if the tweet is in English
                    tweet = {
                        "Review": tweet.text,
                        "lang": tweet.lang
                    }
                    # Send the tweet to the REST API for prediction
                    logging.info("Sending tweet to API...")
                    response = requests.post(api_url, json=tweet["Review"]) # Sends the tweet text to the API for sentiment analysis
                    logging.info("Response from API:", response.json())
        else:
            return "No tweets found."

    except tweepy.TooManyRequests as e:
        logging.info(f"Error: {e}")
        logging.info("Rate limit exceeded. Wait for reset.")

# tweets_data = search_tweets('US Elections')
# print(tweets_data)