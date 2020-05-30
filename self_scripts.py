# -*- coding: utf-8 -*-

import json
import os
import constants

data = {
    "Phone": "18515353986",
    "Password": "57267bd7680e4040f984a0607df80345",
    "ClientId": "10000"
}

s1 = "{\"Phone\":\"18515353986\",\"Password\":\"57267bd7680e4040f984a0607df80345\",\"ClientId\":\"10000\"}"
print(s1)
s2 = json.dumps(data)
print(s2)
print(s2 == s1)
l1 = s2.split(" ")
s3 = ""
for item in l1:
    s3 += item
print(s3)
print(s3 == s1)

print(constants.UToken)
