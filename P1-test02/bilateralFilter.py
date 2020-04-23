# @Description: bilateralFilter.py
# @Author: 孤烟逐云zjy
# @Date: 2020/4/23 11:21
# @SoftWare: PyCharm
# @CSDN: https://blog.csdn.net/zjy123078_zjy
# @博客园: https://www.cnblogs.com/guyan-2020/

import cv2 as cv
import numpy as np


src = cv.imread("./images/raindropGirl.jpg")


# 高斯双边
def bilateralFilter(image):
    # bilateralFilter(src, d, sigmaColor, sigmaSpace, dst=None, borderType=None)
    # sigmaColor: 颜色半径；sigmaSpace：是距离半径；
    dst = cv.bilateralFilter(image, 0, 100, 15)
    # cv.imshow("bilateralFilter image", dst)


# 均值迁移:
def shiftFilter(image):
    dst = cv.pyrMeanShiftFiltering(image, 10, 50)
    # cv.imshow("shift image", dst)


# cv.imshow("Original graph", src)
# bilateralFilter(src)
# shiftFilter(src)


cv.waitKey(0)
cv.destroyAllWindows()