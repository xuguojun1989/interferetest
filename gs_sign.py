# -*- coding: utf-8 -*-

import hashlib
import json
import os


def passwd_md5(passwd, salt):
    m1 = hashlib.md5()
    #  使用md5对象里的update方法md5转换
    m1.update(passwd.encode("utf-8"))
    str1 = m1.hexdigest()
    print(str1)
    str2 = str1 + salt
    m2 = hashlib.md5()
    m2.update(str2.encode("utf-8"))
    passwd2md5 = m2.hexdigest()
    print(passwd2md5)
    return passwd2md5


def generateSignGetbx(params, partner="10016", bxEvn="gaosiedu"):
    # 把{a: 1, b:2}变成 ['a=1', 'b=2']
    li_new = []
    for key, value in params.items():
        li_new.append("{}={}".format(key.lower(), value))
    print(li_new)
    li_new.append("partner={}".format(partner))
    print(li_new)
    li_new.sort()
    print(li_new)
    str1 = ""
    for item in li_new:
        str1 += item + "&"
    print(str1)
    str2 = str1[:-1]
    print(str2)
    str3 = str2 + bxEvn
    print(str3)
    m1 = hashlib.md5()
    #  使用md5对象里的update方法md5转换
    m1.update(str3.encode("utf-8"))
    sign = m1.hexdigest()
    print(sign)
    return sign


def generateSignPost(data, partner="10016", bxEvn="gaosiedu"):
    s2 = json.dumps(data)
    print(s2)
    # l1 = s2.split(" ")
    # s3 = ""
    # for item in l1:
    #     s3 += item
    # print(s3)
    str3 = "partner={}&".format(partner) + s2 + bxEvn
    print(str3)
    m1 = hashlib.md5()
    # 使用md5对象里的update方法md5转换
    m1.update(str3.encode("utf-8"))
    sign = m1.hexdigest()
    print(sign)
    return sign


def f1(str1):
    m1 = hashlib.md5()
    #  使用md5对象里的update方法md5转换
    m1.update(str1.encode("utf-8"))
    sign = m1.hexdigest()
    print(sign)


if __name__ == '__main__':
    # sign: 97acc41c031fd9c67546c8638e63df06

    # params = {
    #     "name": "18515353986"
    # }
    passwd_2 = passwd_md5("000000", "A93B94FC")
    # passwd_2 = passwd_md5("000000", "FEDB0A37")

    #  sign: ab1b2c4462f5c9bcbcc8e0552ce91d4a
    # {\"Phone\":\"18515353986\",\"Password\":\"57267bd7680e4040f984a0607df80345\",\"ClientId\":\"10000\"}
    data = {
        "Phone": "18515353986",
        "Password": passwd_2,
        "ClientId": "10000"
    }
    s = generateSignPost(data=data)
    print(type(s))
    f1(
        "partner=10016&{\"Phone\":\"18515353986\",\"Password\":\"57267bd7680e4040f984a0607df80345\",\"ClientId\":\"10000\"}gaosiedu")
