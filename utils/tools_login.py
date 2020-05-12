import base64


def login_token(username, passwd):
    s = "{}:{}".format(username, passwd)
    a = base64.b64encode(s.encode('utf-8'))
    res = str(a, encoding='utf-8')
    return res


if __name__ == '__main__':
    # res = login_token("13300000015","000015")
    res = login_token("18610865743", "JingYu321")
    print(res)
    'MTg2MTA4NjU3NDM6SmluZ1l1MzIx'
    'MTg2MTA4NjU3NDM6SmluZ1l1MzIx'