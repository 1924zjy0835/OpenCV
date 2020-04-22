# @Description: blur.py
# @Author: 孤烟逐云zjy
# @Date: 2020/4/22 15:10
# @SoftWare: PyCharm
# @CSDN: https://blog.csdn.net/zjy123078_zjy
# @博客园: https://www.cnblogs.com/guyan-2020/

import cv2 as cv
import numpy as np

src = cv.imread("./images/photo01.jpg")


# 均值模糊: 去掉随机噪声
def blur_demo(image):
    dst = cv.blur(image, (5, 5))
    # cv.imshow("blur image", dst)


blur_demo(src)


# 中值模糊（中值滤波）对去除椒盐噪声有很好的作用
# 中值模糊不受异常值的影响，这就是为什么要用它去掉椒盐噪声（异常值）
def median_blur_deno(image):
    # medianBlur(src, ksize, dst=None)
    dst = cv.medianBlur(image, 5)
    # cv.imshow("median image", dst)


# 自定义中值模糊
def custom_blur_demo(image):
    # 此处指定像素值为float32

    # 卷积算子
    # kernel = np.ones([5, 5], np.float32)/25
    # kernel = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]], np.float32) / 9

    # 锐化算子 定义的规则：为奇数，不为奇数的话，就让总和等于0（做边缘和梯度哪些东西），或总和等于1（增强的工作）
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)
    # filter2D(src, ddepth, kernel, dst=None, anchor=None, delta=None, borderType=None)
    dst = cv.filter2D(image, -1, kernel=kernel)

    cv.imshow("custon blur demo", dst)
    cv.imshow("原图 demo", src)


custom_blur_demo(src)

median_blur_deno(src)
cv.waitKey(0)
cv.destroyAllWindows()