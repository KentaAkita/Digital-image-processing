# 2017/8/?
import cv2
import numpy as np
import size
import numba
import matplotlib.pyplot as plt
import time

img = cv2.imread("hoge", 0)

x, y = size.pxsize(img)
start = time.time()


# 全てのピクセル値の合算と、ピクセル値の量
@numba.jit()
def max_def():
    px_total = [0]*256
    px_value_total = 0
    for h in range(y):
        for w in range(x):
            a = img[h][w]
            px_total[a] += 1
            px_value_total += a

    return px_total, px_value_total


# 判別分析法を用いる。クラス間分散を最大にする。
def max_varience():
    px_total, px_value_total = max_def()
    px_sum1 = 0
    px_value_sum1 = 0
    m1 = 0
    px_sum2 =0
    px_value_sum2 = 0
    m2 = 0
    next_varience = 0
    varience = 0
    threshold = 0

    n = 0

    while(n < 255):
        # 初期化処理
        px_sum1 = 0
        px_value_sum1 = 0

        # 黒画素クラス
        for i in range(0, n + 1):
            px_sum1 += px_total[i]
            px_value_sum1 += i*px_total[i]

        if px_sum1 != 0:
            m1 = px_value_sum1/px_sum1

        # 白画素クラス
        px_sum2 = x*y - px_sum1
        px_value_sum2 = px_value_total - px_value_sum1
        m2 = px_value_sum2/px_sum2

        next_varience = (px_sum1*px_sum2*(m1-m2)*(m1-m2))/((x*y)**2)

        if varience < next_varience:
            varience = next_varience
            threshold = n
            print(n)

        n += 1

    return threshold


# 2値化処理
def binarization():
    x, y = size.pxsize(img)
    t = max_varience()

    # ｔで黒白分類
    for h in range(y):
        for w in range(x):
            if img[h][w] <= t:
                img[h][w] = 0

            else:
                img[h][w] = 255


def main():  # 全ての処理を行う。
    binarization()
    cv2.imshow('differential', img)
    elapsed_time = time.time() - start
    print(elapsed_time)
    cv2.waitKey()
    cv2.destroyAllWindow()


main()  # 実行
