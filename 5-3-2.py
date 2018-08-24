# 2017/7/?
import cv2
import numpy as np
import math

img = cv2.imread("hoge")  # 画像の読み込みと読み込んだ色のタイプを指定
img2 = cv2.imread("hoge")  # 画像の読み込みと読み込んだ色のタイプを指定

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)    # グレースケールにする。


def r():  # 画像サイズを取得し、rangeでint型に変更する。
    n = len(img[1])
    i = len(img)
    return (n, i)


def differential():     # 微分フィルタ
    n, i = r()

    edge = [[0 for i in range(n)] for j in range(i)]

    # 以下は横方向の微分フィルタ。白黒で表示する。
    for h in range(i):
        for w in range(n-1):
            if gray[h][w] > (gray[h][w+1] + 10):    # 右隣と比較し、大きければ青色表示。
                img[h][w+1] = [255, 255, 255]

            else:   # 変化がないところは黒色にする。
                img[h][w+1] = [0, 0, 0]

    # 以下は縦方向の微分フィルタ。
    """for h in range(i-1):
        for w in range(n):
            if gray[h][w] > (gray[h+1][w] + 10):
                img[h+1][w] = [255, 255, 255]

            else:
                img[h+1][w] = [0, 0, 0]"""


def sobel():
    global w
    differential()
    n, i = r()

    times_w = int(n/3)  # 平滑化する際の範囲の設定
    times_h = int(i/3)
    average_y = [[0 for i in range(n)] for j in range(times_h)]
    average_x = [[0 for i in range(times_w)] for j in range(i)]
    x = 0
    y = 0
    # 縦方向の平滑化
    for h in range(i):
        for w in range(n):
            average_y[y][w] += img[h][w]
        if h % 3 == 2:
            y += 1
    y = 0
    for h in range(i):
        for w in range(n):
            if i % 3 == 1:
                if y % 3 == 1:
                    img[h][w] = (1/2)*average_y[y][w]

                else:
                    img[h][w] = (1/4)*average_y[y][w]
            if h % 3 == 2:
                y += 1
    """for h in range(i):
        for w in range(n):
            average_x[h][x] += img[h][w]
            if w % 3 == 2:
                x += 1
    x = 0
    for h in range(i):
        for w in range(n):  # RGB各チャンネルの値の合計を平均して戻す。
            if x % 3 == 1:
                img[h][w] = (1/2)*average_x[h][x]

            else:
                img[h][w] = (1/4)*average_x[h][x]
            if w % 3 == 2:
                x += 1"""


def main():  # 全ての処理を行う。
    sobel()
    cv2.imshow('gauss', img)
    cv2.waitKey()
    cv2.destroyAllWindow()


main()  # 実行