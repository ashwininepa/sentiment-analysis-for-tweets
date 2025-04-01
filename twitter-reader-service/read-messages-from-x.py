import tweepy
import os
import requests


# Set up Twitter API credentials
API_KEY = os.getenv('TWITTER_API_KEY')
API_SECRET_KEY = os.getenv('TWITTER_API_SECRET_KEY')
ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')

# Send tweets to the REST API
api_url = "http://api_service:5000/predict"

# Authenticate to Twitter API
client = tweepy.Client(bearer_token=BEARER_TOKEN)

def search_tweets(query, max_results=100):
    try:
        # Search for tweets matching the query
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
                    response = requests.post(api_url, json=tweet["Review"])
                    print("Response from API:", response.json())
        else:
            return "No tweets found."

    except tweepy.TooManyRequests as e:
        print(f"Error: {e}")
        print("Rate limit exceeded. Wait for reset.")

# tweets_data = search_tweets('US Elections')
# print(tweets_data)