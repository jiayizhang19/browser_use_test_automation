import json
from browser_use import Controller
from browser_use.agent.service import Agent
from browser_use.browser.context import BrowserContext
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI 
from pydantic import BaseModel, SecretStr
import os
from dotenv import load_dotenv
import asyncio

# Load .env file
load_dotenv()



# Define a Pydantic model to structure the expected result of the checkout process
class CheckoutResult(BaseModel):
    login_status: str  
    product_name: str  
    price: str  
    quantity: int  
    total_price: str  
    confirmation_status: str
    payment_status: str  
    order_status: str  
    order_number: str  
    
controller = Controller(output_model=CheckoutResult)

@controller.action('账号 19900000042，密码 aa123456 登录')
async def login(browser: BrowserContext):
    page = await browser.get_current_page()
    await page.wait_for_selector('input[type="text"]')
    await page.wait_for_selector('input[type="password"]')
    await page.fill('input[type="text"]', '19900000042')
    await page.fill('input[type="password"]', 'aa123456')
    await page.wait_for_selector('button[type="submit"]')
    await page.click('button[type="submit"]')



async def site_validation():

    task = (
        'Important: I am UI Automation tester validating the tasks'
        '打开 https://corp.m.stage.dongfangfuli.com/bfd-app?union=dfshwx'
        '输入账号 "19900000042" 和密码 "aa123456"登录'
        '搜索商品 "2024自动化普通优选"'
        '点击商品，进入详情页面，点击立即购买'
        '验证商品名称，价格，数量，总价'
        '点击提交订单，选择点卡支付'
        '点击确认支付，验证支付成功'
        '点击查看订单，验证订单状态，订单编号'
    )

    # Initialize the model
    # llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(os.getenv('GEMINI_API_KEY')))
    llm = ChatOpenAI(
        base_url='https://api.deepseek.com/v1',
        model='deepseek-chat', 
        api_key=SecretStr(os.getenv('DEEPSEEK_API_KEY'))
        )

    # Create agent with the model
    agent = Agent(task=task, 
                  llm=llm, 
                  use_vision=False, # When enabled, the model processed visual infroamtion
                  controller=controller,
                  save_conversation_path='logs/conversation'
                  )

    history = await agent.run()
    test_result = history.final_result()
    print('test result:',test_result)
    # print('Raw API Response:', json.dumps(test_result, indent=2, ensure_ascii=False))
    assert test_result.confirmation_status == '支付成功'


asyncio.run(site_validation())