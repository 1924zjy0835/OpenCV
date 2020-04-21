# @Description: pixel.py
# @Author: 孤烟逐云zjy
# @Date: 2020/4/21 7:21
# @SoftWare: PyCharm
# @CSDN: https://blog.csdn.net/zjy123078_zjy
# @博客园: https://www.cnblogs.com/guyan-2020/

import cv2 as cv
import numpy as np


print("-------------2020/4/21 像素运算操作")
# src1 = cv.imread("./images/WindowsLogo.jpg")
# src2 = cv.imread("./images/LinuxLogo.jpg")
# src3 = cv.imread("./images/photo01.jpg")
# cv.imshow("windows logo", src1)
# cv.imshow("linux logo", src2)
# print(src1.shape)
# print(src2.shape)

"""
# 对图片进行运算叠加操作
def add_image_demo(image1, image2):
    dst = cv.add(image1, image2)
    cv.imshow("dst logo", dst)


add_image_demo(src1, src2)
"""

"""
# 对图片进行相减操作
def subtract_image_demo(image1, image2):
    sub_dst = cv.subtract(image1, image2)
    cv.imshow("subtract image", sub_dst)


subtract_image_demo(src1,src2)
"""

"""
# 对图片进行相减操作
def divide_image_demo(image1, image2):
    divide_dst = cv.divide(image1, image2)
    cv.imshow("divide image", divide_dst)


divide_image_demo(src2, src1)
"""

"""
# 对图片做相乘操作
def multiply_image_demo(image1, image2):
    divide_dst = cv.multiply(image1, image2)
    cv.imshow("divide image", divide_dst)


multiply_image_demo(src2, src1)
"""

"""
def others_demo(image1, image2):
    m1 = cv.mean(image1)
    m2 = cv.mean(image2)

    print("M1: %s,M2: %s"%(m1,m2))


others_demo(src1, src2)
"""

"""
def others_demo(image1, image2):
    m1 = cv.meanStdDev(image1)
    m2 = cv.meanStdDev(image2)
    print("M1: %s,M2: %s"%(m1,m2))


others_demo(src2, src1)
"""


"""
# guyan01 = cv.imread("./images/guyan01.jpg")


# 逻辑运算
def bitwise_not_demo(image1):
    not_image = cv.bitwise_not(image1)
    cv.imshow("Not Image demo", not_image)


bitwise_not_demo(guyan01)
"""


"""
# 调整图片的对比度和亮度  addWeighted(src1, alpha, src2, beta, gamma, dst=None, dtype=None)
def contrast_brightness_demo(image, c, b):
    h, w, ch = image.shape
    image_blank = np.zeros([h, w, ch], image.dtype)
    dst_image = cv.addWeighted(image, c, image_blank, 1-c, b)
    cv.imshow("constrast brightness image", dst_image)


contrast_brightness_demo(src3, 1.2, 50)
"""
cv.waitKey(0)
cv.destroyAllWindows()
