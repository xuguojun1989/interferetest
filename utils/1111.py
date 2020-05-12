
import base64
s = '13300000015:000015'
a = base64.b64encode(s.encode('utf-8'))
b = str(a,encoding='utf-8')
print(b)
# MTMzMDAwMDAwMTU6MDAwMDE1  生成
# MTMzMDAwMDAwMTU6MDAwMDE1

data = {"common":
            {"_aKey": "jingyuxiaoban-windows",
             "_vName": "2.2.3",
             "_pName": "鲸鱼学堂",
             "_vOs": "Win10",
             "_lang": "zh-cn",
             "_vApp": "2.2.3",
             "_nId": "wifi",
             "_t": 123
             }
        }

data.update({
    "name":"gusiyuan"
})
print(data)
