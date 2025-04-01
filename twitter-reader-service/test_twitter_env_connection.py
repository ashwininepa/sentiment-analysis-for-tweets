import tweepy
import os

import pandas as pd

# Set up Twitter API credentials
API_KEY = os.getenv('TWITTER_API_KEY')
API_SECRET_KEY = os.getenv('TWITTER_API_SECRET_KEY')
ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')

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
            tweets = []
            for tweet in response.data:
                tweets.append({
                    "Review": tweet.text,
                    "lang": tweet.lang
                })
                
            tweets_df = pd.DataFrame(tweets)
            # Keep only english text
            tweets_df = tweets_df[tweets_df['lang'] == 'en']
            
            return tweets_df
        else:
            print("No tweets found.")
            return pd.DataFrame()

    except tweepy.TooManyRequests as e:
        print(f"Error: {e}")
        print("Rate limit exceeded. Wait for reset.")

tweets_data = search_tweets('US Elections')
print(tweets_data)