# 2017/6/?
import cv2
import numpy as np
import size
import time

start = time.time()

img = cv2.imread("hoge")  # 画像の読み込みと読み込んだ色のタイプを指定


gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)    # グレースケールにする。

x, y = size.pxsize(img)

a = np.array([[0]]*y)

d_gray = np.c_[a, gray]    # 微分するために一つずらす
d_gray = np.delete(d_gray, x, 1)    # 引き算するために最後の行を消して次元を要素をそろえる。
diff = d_gray - gray  # 差をとり、正負で判定する。


def differential():     # 微分フィルタ
    x, y = size.pxsize(img)

    # 以下は横方向の微分フィルタ。
    for h in range(y):
        for w in range(1, x):
            if diff[h][w] > 10:    # 右隣と比較し、大きければ青色表示。
                img[h][w] = [255, 0, 0]

            elif diff[h][w] < -10:  # 右隣と比較し、小さければ緑色表示。
                img[h][w] = [0, 255, 0]

            else:   # 変化がないところは黒色にする。
                img[h][w] = [0, 0, 0]

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


def main():  # 全ての処理を行う。
    differential()
    cv2.imshow('differential', img)
    elapsed_time = time.time() - start
    print(elapsed_time)
    cv2.waitKey()
    cv2.destroyAllWindow()


main()  # 実行