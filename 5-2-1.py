# 2017/6/?
import cv2
import numpy as np
import size
import time
from multiprocessing import Pool
import multiprocessing as ml


img = cv2.imread("hoge")  # 画像の読み込みと読み込んだ色のタイプを指定
x, y = size.pxsize(img)


def smoothing_color():  # 平滑化
    global img
    average = np.array([[[0 for k in range(3)] for i in range(x)] for j in range(y)])
    times_w = int(x/5)
    times_h = int(y/5)

    for i in range(times_h):
        for j in range(times_w):
            average[5*i:5*(i+1), 5*j:5*(j+1), 0:1] = (1/25)*np.sum(img[5*i:5*(i+1), 5*j:5*(j+1), 0:1])
            average[5 * i:5 * (i + 1), 5 * j:5 * (j + 1), 1:2] = (1 / 25) * np.sum(img[5 * i:5 * (i + 1), 5 * j:5 * (j + 1), 1:2])
            average[5 * i:5 * (i + 1), 5 * j:5 * (j + 1), 2:3] = (1 / 25) * np.sum(img[5 * i:5 * (i + 1), 5 * j:5 * (j + 1), 2:3])

    img = np.uint8(average)


def main():  # 全ての処理を行う。
    if __name__ == "__main__":
        start = time.time()
        smoothing_color()
        end = time.time() - start
        print(end)
        gray = False

        if gray == True:
            gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            cv2.imshow('average', gray_img)
            cv2.waitKey()
            cv2.destroyAllWindow()

        else:
            cv2.imshow('average', img)
            cv2.waitKey()
            cv2.destroyAllWindow()
            

main()
