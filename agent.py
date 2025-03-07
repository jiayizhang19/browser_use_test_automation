
from browser_use.agent.service import Agent
from langchain_openai import ChatOpenAI
from pydantic import SecretStr
from dotenv import load_dotenv
import os

load_dotenv()

def initialize_agent(task):

    llm = ChatOpenAI(
        base_url='https://api.deepseek.com/v1',
        model='deepseek-chat', 
        api_key=SecretStr(os.getenv('DEEPSEEK_API_KEY'))
        )
    
    agent = Agent(task=task, llm=llm, use_vision=False, save_conversation_path='logs/conversation')
    
    return agent
