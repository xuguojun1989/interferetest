# -*- coding: utf-8 -*-

import hashlib
import json


def generateSignGetbx(params, bxEvn, partner):
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

if __name__ == '__main__':
    # sign: a3795ec60d958c49e8962a0770396fb1

    params = {
        "name": "13387836885"
    }
    generateSignGetbx(params=params, bxEvn="gaosiedu", partner="10016")
