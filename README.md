# Twitter API Project

## Overview
This project provides a simple way to interact with the Twitter API using Python. It utilizes the Tweepy library to authenticate with Twitter, fetch user tweets, post new tweets, search for tweets, and follow users. This repository is structured to ensure secure storage of API credentials using environment variables.

## Features
- Authenticate using Twitter API keys securely
- Fetch the latest tweets from a specified user
- Post tweets directly from your Python script
- Search for tweets based on keywords
- Follow users programmatically
- Ensure API keys are kept secure using a `.env` file

## Prerequisites
Before setting up this project, ensure you have:
- A Twitter Developer Account ([Sign up here](https://developer.twitter.com/))
- Python installed (version 3.6 or higher recommended)
- An active Twitter App with API keys and tokens

## Steps to Access Twitter API and Obtain API Keys
### 1. Create a Twitter Developer Account
- Visit the [Twitter Developer Portal](https://developer.twitter.com/).
- Sign in with your Twitter account.
- Apply for a **Developer Account** by selecting your intended use case (Personal Project, Research, Business, etc.).
- Once approved, navigate to **Developer Portal → Projects & Apps**.

### 2. Create a Twitter App
- Click **Create an App**.
- Provide the necessary details (App Name, Description, Website URL, etc.).
- Choose the required **API access level**:
  - **Essential (Free)**: Limited access, read-only.
  - **Elevated**: More access, requires approval.
  - **Academic/Enterprise**: Advanced access.
- After creation, navigate to the **Keys and Tokens** tab.

### 3. Generate API Keys & Tokens
You will receive the following credentials:
- **Consumer API Key & Secret** – Used for authentication.
- **Access Token & Secret** – Grants access to specific Twitter account actions.
- **Bearer Token** – Used for making requests to Twitter API v2.

**Important:** Store these securely and **never expose them in public repositories!**

## Installation
### 1. Clone the Repository
Open a terminal and run:
```bash
git clone https://github.com/yourusername/twitter-api-project.git
cd twitter-api-project
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies
Install the required Python packages using:
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the project directory and add your Twitter API credentials:
```plaintext
API_KEY=your-api-key
API_SECRET=your-api-secret
ACCESS_TOKEN=your-access-token
ACCESS_SECRET=your-access-secret
```

**Important:** Never share your `.env` file publicly.

### 5. Run the Script
Execute the script to fetch the latest tweets:
```bash
python twitter_api_script.py
```

## API Functions
### Authenticate with Twitter
```python
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
```

### Fetch Latest Tweets from a User
```python
username = "TwitterDev"
tweets = api.user_timeline(screen_name=username, count=5)
for tweet in tweets:
    print(tweet.text)
```

### Post a Tweet
```python
api.update_status("Hello, Twitter API! #MyFirstTweet")
```

### Search for Tweets
```python
search_results = api.search_tweets(q="OpenAI", count=5)
for tweet in search_results:
    print(tweet.text)
```

### Follow a User
```python
api.create_friendship(screen_name="elonmusk")
```

## Notes
- Be mindful of Twitter API rate limits.
- Read the [Twitter API Docs](https://developer.twitter.com/en/docs) for more capabilities.
- Store credentials securely and **never hardcode them** in your script.

## License
This project is licensed under the MIT License. See `LICENSE` for more details.

---
🚀 **Happy Coding!**
