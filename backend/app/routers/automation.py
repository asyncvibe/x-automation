from fastapi import APIRouter
from pydantic import BaseModel
from ..services import autogen_service, twitter_service

router = APIRouter()

class TweetRequest(BaseModel):
    prompt: str

@router.post("/generate-and-post-tweet")
async def generate_and_post(request: TweetRequest):
    # Step 1: Generate content with AutoGen
    tweet_text = autogen_service.generate_tweet_content(request.prompt)

    # Add some error handling here in a real app
    if not tweet_text or "TERMINATE" in tweet_text:
         return {"status": "error", "message": "Failed to generate tweet content."}

    # Step 2: Post the generated content to Twitter
    result = twitter_service.post_tweet(tweet_text)

    return {"generated_text": tweet_text, "post_result": result}