# 2017/9/?
import cv2
import numpy as np
import size
import time

img = cv2.imread("hoge", 0)
img2 = cv2.imread("hoge", 0)

x, y = size.pxsize(img)


def variance_px():
    sides_x = 5
    sides_y = 5
    start_x = 0
    start_y = 0

    average = [[0 for i in range(x - (sides_x-1))] for j in range(y - (sides_y-1))]
    variance = [[0 for i in range(x - (sides_x-1))] for j in range(y - (sides_y-1))]

    for w in range(x - (sides_x-1)):
        for h in range(y - (sides_y-1)):
            for b in range(start_x, sides_x + start_x):
                for a in range(start_y, sides_y + start_y):
                    average[h][w] += img[a][b]

            average[h][w] = int((1 / (sides_y * sides_x)) * average[h][w])
            start_y += 1
        start_y = 0
        start_x += 1

    start_x = 0
    start_y = 0
    for w in range(x - (sides_x-1)):
        for h in range(y - (sides_y-1)):
            for b in range(start_x, sides_x + start_x):
                for a in range(start_y, sides_y + start_y):
                    variance[h][w] += (img[a][b] - average[h][w]) ** 2

            variance[h][w] = int((1 / (sides_x * sides_y)) * variance[h][w])
            start_y += 1
        start_y = 0
        start_x += 1

    return variance


# 5*5のバイラテラルフィルタ
def bilateral():
    w = 0
    sig_sp = 3
    sig_px = variance_px()
    att_px_x = 2
    att_px_y = 2
    m = -2
    n = -2

    a = [[0 for i in range(x - 4)] for j in range(y - 4)]
    b = [[0 for i in range(x - 4)] for j in range(y - 4)]

    sides_x = 5
    sides_y = 5
    start_x = 0
    start_y = 0

    for g_x in range(x - 4):
        for g_y in range(y - 4):
            for i in range(att_px_x - 2, att_px_x + 3):
                for j in range(att_px_y - 2, att_px_y + 3):
                    if sig_px[g_y][g_x] > 0:
                        w = np.exp(-(m * m + n * n) / (2 * sig_sp ** 2)) * \
                            np.exp(-((img[att_px_y][att_px_x] - img[j][i]) ** 2) / (2 * sig_px[g_y][g_x]))

                        a[g_y][g_x] += w * img[j][i]
                        b[g_y][g_x] += w
                        n += 1
                    n = -2
                    m += 1
                m = -2
            att_px_y += 1
        att_px_y = 2
        att_px_x += 1

    for w in range(x - 4):
        for h in range(y - 4):
            for i in range(start_x, sides_x + start_x):
                for j in range(start_y, sides_y + start_y):
                    if 0 < b[h][w]:
                        img[j][i] = int(a[h][w] / b[h][w])
            start_y += 1
        start_y = 0
        start_x += 1


def main():
    start = time.time()
    bilateral()
    end = time.time() - start
    print(end)
    print(img)
    print(img2)
    cv2.imshow("bilateral", img)
    cv2.imshow("gray", img2)
    cv2.waitKey()
    cv2.destroyAllWindow()

main()
