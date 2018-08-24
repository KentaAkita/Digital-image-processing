# 2017/7/?
import cv2
import numpy as np
import math

img = cv2.imread("hoge", 0)  # 画像の読み込みと読み込んだ色のタイプを指定
img2 = cv2.imread("hoge", 0)  # 画像の読み込みと読み込んだ色のタイプを指定


def r():  # 画像サイズを取得し、rangeでint型に変更する。
    n = len(img[1])
    i = len(img)
    return (n, i)


def smoothing():  # 平滑化
    n, i = r()
    times_w = int(n / 5)  # 平滑化する際の範囲の設定
    times_h = int(i / 5)
    average = [[0 for i in range(times_w)] for j in range(times_h)]
    x = 0
    y = 0
    for h in range(i):
        x = 0
        for w in range(n):  # RGB各チャンネルの合計を取る。
            average[y][x] += img[h][w]
            if w % 5 == 4:  # 次の範囲への移動
                x += 1
        if h % 5 == 4:
            y += 1
    y = 0
    for h in range(i):
        x = 0
        for w in range(n):  # RGB各チャンネルの値の合計を平均して戻す。
            img[h][w] = (1 / 25) * average[y][x]  # 係数は面積
            if w % 5 == 4:
                x += 1
        if h % 5 == 4:
            y += 1


def sharpening():  # 鮮鋭化
    n, i = r()
    k = 2  # 係数倍する。
    img_sharpening = [[0 for i in range(n)] for j in range(i)]
    for h in range(i):
        for w in range(n):  # RGB各チャンネルの合計を取る。
            if img[h][w] > img2[h][w]:  # overflowして-が+になってしまうことを防ぐ。
                img_sharpening[h][w] = int(img[h][w] - img2[h][w])

            else:  # -になる場合は0を代入する。
                img_sharpening[h][w] = 0

    for h in range(i):
        for w in range(n):
            if (img2[h][w] + k * img_sharpening[h][w] <= 255):  # Overflowしてしまうのを防ぐ。
                img2[h][w] += k * img_sharpening[h][w]  # 先鋭化するために目立つ部分をk倍して加算する。

            else:
                img2[h][w] = 255


def main():  # 全ての処理を行う。
    smoothing()
    sharpening()
    cv2.imshow('sharpening', img2)
    cv2.waitKey()
    cv2.destroyAllWindow()


main()  # 実行
