import tweepy
from ..core.config import settings

def post_tweet(text: str) -> dict:
    try:
        client = tweepy.Client(
            consumer_key=settings.twitter_api_key,
            consumer_secret=settings.twitter_api_secret_key,
            access_token=settings.twitter_access_token,
            access_token_secret=settings.twitter_access_token_secret
        )
        response = client.create_tweet(text=text)
        return {"status": "success", "tweet_id": response.data['id']}
    except Exception as e:
        # Log the error properly in a real application
        print(f"Error posting tweet: {e}")
        return {"status": "error", "message": str(e)}