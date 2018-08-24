# 2017/10/1
import cv2
import numpy as np
import size

img = cv2.imread("hoge")
img2 = cv2.imread("hoge")

a = np.uint8(img/2 + img2/2)
x, y = size.pxsize(img)


def alpha_blending():
    k = 0
    for i in range(x):
        k = i/x
        img[:, i:i+1] = np.uint8(k*img[:, i:i+1] + (1-k)*img2[:, i:i+1])


def emboss():
    size = tuple(np.array([x, y]))
    transx = 1
    transy = 1
    matrix = np.float32([[1, 0, transx], [0, 1, transy]])
    gray_img = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)
    np_img = 255 - gray_img
    a = 0

    affine_img = cv2.warpAffine(np_img, matrix, size)
    emboss_img = np.float32(affine_img) - 128 + np.float32(gray_img)

    emboss_img = np.where(emboss_img > 255, 255, emboss_img)
    emboss_img = np.where(emboss_img < 0, 0, emboss_img)

    emboss_img = np.uint8(emboss_img)

    return emboss_img


def main():
    select = 1
    if select == 0:
        cv2.imshow("blending", a)

    elif select == 1:
        alpha_blending()
        cv2.imshow("alpha blending", img)

    elif select == 2:
        e_img = emboss()
        cv2.imshow("emboss", e_img)

    cv2.waitKey()
    cv2.destroyAllWindows()

main()
