import autogen
from ..core.config import settings

def generate_tweet_content(prompt: str) -> str:
    config_list = [{"model": "gpt-4", "api_key": settings.openai_api_key}]

    llm_config = {
        "config_list": config_list,
        "temperature": 0.7,
    }

    copywriter = autogen.AssistantAgent(
        name="Copywriter",
        system_message="You are a professional social media copywriter specializing in creating concise, engaging, and viral tweets. Your output should be ONLY the tweet text, without any extra commentary.",
        llm_config=llm_config,
    )

    user_proxy = autogen.UserProxyAgent(
        name="user_proxy",
        human_input_mode="NEVER",
        max_consecutive_auto_reply=1,
        is_termination_msg=lambda x: True, # Terminate after one response
    )

    # Start the conversation
    user_proxy.initiate_chat(
        recipient=copywriter,
        message=f"Generate a tweet based on this prompt: {prompt}. The tweet must be under 280 characters.",
    )
    # The last message from the chat history will be the tweet
    final_response = user_proxy.last_message()["content"]
    return final_response