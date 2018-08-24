# 20177/6/?
import cv2
import numpy as np
import math
import size
import time

img = cv2.imread("hoge")  # 画像の読み込みと読み込んだ色のタイプを指定
img2 = cv2.imread("hoge")  # 画像の読み込みと読み込んだ色のタイプを指定


x, y = size.pxsize(img)


def gauss_weight():    # 5*5のガウシアンフィルタ
    times_w = int(x/5)
    times_h = int(y/5)
    # varience = np.array([[[0 for k in range(3)]for i in range(times_w)] for j in range(times_h)])
    g = np.array([[[0 for i in range(3)]for k in range(5)]for j in range(5)], dtype=float)
    varience = 1

    for i in range(-2, 3):
        for j in range(-2, 3):
            g[i+2][j+2] = np.float64(((1/(2*math.pi*varience**2))*np.exp(-(i**2 + j**2)/(2*varience**2))))

    return g


def smoothing():
    g = gauss_weight()
    global img

    for j in range(2, y-2):
        for i in range(2, x-2):
            img[j][i] = np.sum(img2[j-2:j+3, i-2:i+3, 0:1] * g[:, :, 0:1])
            img[j][i][1] = np.sum(img2[j - 2:j + 3, i - 2:i + 3, 1:2] * g[:, :, 1:2])
            img[j][i][2] = np.sum(img2[j - 2:j + 3, i - 2:i + 3, 2:3] * g[:, :, 2:3])


def main():  # 全ての処理を行う。
    start = time.time()
    smoothing()
    end = time.time()
    gray = False

    print(end - start)

    if gray == True:
        gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        cv2.imshow('gauss', gray_img)
        cv2.waitKey()
        cv2.destroyAllWindow()

    else:
        cv2.imshow('gauss', img)
        cv2.waitKey()
        cv2.destroyAllWindow()


main()  # 実行
