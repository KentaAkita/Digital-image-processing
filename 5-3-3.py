# 2017/7/?
import cv2
import numpy as np
import math

img = cv2.imread("hoge")  # 画像の読み込みと読み込んだ色のタイプを指定
img2 = cv2.imread("hoge")  # 画像の読み込みと読み込んだ色のタイプを指定

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)  # グレースケールにする。


def r():  # 画像サイズを取得し、rangeでint型に変更する。
    n = len(img[1])
    i = len(img)
    return (n, i)


def differential1():  # 微分フィルタ
    n, i = r()

    edge = [[[0 for k in range(3)] for i in range(n)] for j in range(i)]

    # 以下は横方向の微分フィルタ。
    for h in range(i):
        for w in range(n - 1):
            if gray[h][w] > (gray[h][w + 1] + 10):  # 右隣と比較し、大きければ青色表示。
                edge[h][w + 1] = [255, 0, 0]

            elif gray[h][w] < (gray[h][w + 1] - 10):  # 右隣と比較し、小さければ緑色表示。
                edge[h][w + 1] = [0, 255, 0]

            else:  # 変化がないところは黒色にする。
                edge[h][w + 1] = [0, 0, 0]

    # 以下は縦方向の微分フィルタ。
    """for h in range(i-1):
        for w in range(n):
            if gray[h][w] > gray[h+1][w]:
                img[h+1][w] = [255, 0, 0]

            elif gray[h][w] < gray[h+1][w]:
                img[h+1][w] = [0, 255, 0]

            elif gray[h][w] == gray[h+1][w]:
                img[h+1][w] = [0, 0, 0]
"""

    return edge


def differential2():
    n, i = r()

    edge = [[[0 for k in range(3)] for i in range(n)] for j in range(i)]

    # 以下は横方向の微分フィルタ。
    for h in range(i):
        for w in range(1, n):
            if gray[h][w] > (gray[h][w - 1] + 10):  # 右隣と比較し、大きければ青色表示。
                edge[h][w - 1] = [255, 0, 0]

            elif gray[h][w] < (gray[h][w - 1] - 10):  # 右隣と比較し、小さければ緑色表示。
                edge[h][w - 1] = [0, 255, 0]

            else:  # 変化がないところは黒色にする。
                edge[h][w - 1] = [0, 0, 0]

    return edge


def final():
    a1 = differential1()
    a2 = differential2()
    n, i = r()

    for h in range(i):
        for w in range(n):
            if (a1[h][w][0] == 255) or (a2[h][w][0] == 255):
                img[h][w][0] = abs(a1[h][w][0] - a2[h][w][0])

            elif(a1[h][w][1] == 255) or (a2[h][w][1] == 255):
                img[h][w][1] = abs(a1[h][w][1] - a2[h][w][1])

            else:
                img[h][w] = [0, 0, 0]


def main():  # 全ての処理を行う。
    final()
    cv2.imshow('differential', img)
    cv2.waitKey()
    cv2.destroyAllWindow()


main()  # 実行
