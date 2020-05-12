# -*- coding: utf-8 -*-
import requests

from utils.tools_print import better_print
import constant

host = constant.HOST
api = "/reg/api/v3/SMS/QueryVerificationCode"
# api = "/reg/api/v3/SMS/QueryVerificationCode?phone=18515353986&type=0"
url = host + api
print(url)

# 头部常规参数：
content_type = constant.CONTENT_TYPE1
user_agent = constant.USER_AGENT
# 头部签名参数
usrSign = {
    "13387836887": constant.SIGN1,
    "18515353986": constant.SIGN2
}
partner = constant.PARTNER
# get请求参数 0-登录
type = "0"
# k:手机号，v:签名
phone = "18515353986"
sign = usrSign[phone]

headers = {
    "sign": sign,
    "partner": partner,
    "content-type": content_type,
    "User-Agent": user_agent
}
params = {
    "phone": phone,
    "type": type

}
res = requests.get(url=url, params=params, headers=headers)
print(better_print(res.content))
# print(better_print(res.text))
# print(res.status_code)
