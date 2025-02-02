from huggingface_hub import InferenceClient

from config import HF_API_KEY
from logger import get_logger

logger = get_logger()

HF_API_KEY= HF_API_KEY 


class ChatLexi:
    def __init__(self, model="deepseek-ai/DeepSeek-R1", context_text: str = "You are Lexi, your name is lexi and my name your creator is Kashif Khan, my personal AI assistant, helping me with various tasks and queries. only I will be interact with you so you can talk to me like friend and make joke with me when i message you to start"):
        self.client = InferenceClient(provider="together", api_key=HF_API_KEY)
        self.model = model
        self.messages = []
        if context_text:
            self.messages.append({"role": "system", "content": context_text})

    def chat(self, message: str):
        logger.info("chat initiated")
        self.messages.append({"role": "user", "content": message})
        completion = self.client.chat.completions.create(
            model=self.model, messages=self.messages, max_tokens=500
        )
        response = completion.choices[0].message 
        response_content = response["content"]
        
        think_text = ""
        actual_response = response_content
        if "<think>" in response_content and "</think>" in response_content:
            think_text = response_content.split("<think>")[1].split("</think>")[0].strip()
            actual_response = response_content.split("</think>")[1].strip()
        
        self.messages.append({"role": "assistant", "content": actual_response})
        
        return {
            "role": response["role"],
            "think": think_text,
            "response": actual_response,
            "full_response": response
        }

