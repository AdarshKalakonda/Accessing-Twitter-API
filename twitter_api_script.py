import tweepy
import os
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Fetch latest tweets from a user
username = "TwitterDev"
tweets = api.user_timeline(screen_name=username, count=5)

for tweet in tweets:
    print(tweet.text)
