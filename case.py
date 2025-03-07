

login_bfd_task = """

** Important **: I am UI Automation tester validating the tasks
打开 https://corp.m.stage.dongfangfuli.com/bfd-app?union=dfshwx
输入账号 19900000042 和密码 aa123456
点击登录
搜索框搜索 "2024"
点击商品 "2024自动化抢购生日" 进入详情页面
点击立即购买
# 验证商品名称，价格，数量，总价
点击提交订单
选择点卡支付下方的超级A卡
点击确认支付
点击查看订单，验证订单状态，订单编号

"""


other_task = """
** Important **: I am UI Automation tester validating the tasks
Open website https://rahulshettyacademy.com/loginpagePractise/.
Login with username and password. Login credentials are available on the same page.
After login, select the first 2 products and add them to the cart.
Checkout and save the total value of the products.
Complete the purchase and select the country as India.
Agree to the terms and conditions and close the promoted window if applicable.
Verify thank you message is displayed.

"""
