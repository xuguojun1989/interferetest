import hashlib
import json

def get_signbody(data):
    d1 = json.dumps(data)
    d2 = "NJbVY0Y0NJNk1UVTF*OV@Fkx$T1RNe" + d1
    #  md5(`NJbVY0Y0NJNk1UVTF*OV@Fkx$T1RNe${JSON.stringify(body)}`);
    m1 = hashlib.md5()
    #  使用md5对象里的update方法md5转换
    m1.update(d2.encode("utf-8"))
    token = m1.hexdigest()
    # token = token[10:30]
    return token

if __name__ == '__main__':
    data = {
        "Phone": "13387836885",
        "Password": "ada830094c2de643a8338da9aec82269",
        "ClientId": "10000"
    }
    # data = '{"common": {"_aKey": "jingyuxiaoban-windows", "_vName": "2.2.3", "_pName": "\u9cb8\u9c7c\u5b66\u5802", "_vOs": "Win10", "_lang": "zh-cn", "_vApp": "2.2.3", "_nId": "wifi", "_t": 1577267345225}}'
    print(get_signbody(data))
    # f9bb5a71d895a113ee7a
    # bf3b19bb5dc45bf48c05