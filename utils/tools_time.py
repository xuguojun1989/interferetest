import time
# 1576733341391
# 1577154533671
def time_tran():
    t = time.time()
    return int(round(1000*t))


if __name__ == '__main__':
    t = time_tran()
    print(t)
    # 1583734208532
    # 1583733749277