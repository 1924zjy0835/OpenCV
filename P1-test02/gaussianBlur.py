# @Description: gaussianBlur.py
# @Author: 孤烟逐云zjy
# @Date: 2020/4/23 9:21
# @SoftWare: PyCharm
# @CSDN: https://blog.csdn.net/zjy123078_zjy
# @博客园: https://www.cnblogs.com/guyan-2020/

import cv2 as cv
import numpy as np


def clamp(value):
    if value > 255:
        return 255
    elif value < 0:
        return 0
    else:
        return value


def Gaussian_noise(image):
    h, w, c = image.shape
    # 遍历每一个像素点，为其加上一个随机数的值，就可以得到高斯值
    for row in range(h):
        for col in range(w):
            # normal(loc=0.0, scale=1.0, size=None)，三个参数分别代表的是随机数的均值、方差以及输出的size
            random_value = np.random.normal(0, 20, 3)
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]

            image[row, col, 0] = clamp(b + clamp(random_value[0]))
            image[row, col, 1] = clamp(b + clamp(random_value[1]))
            image[row, col, 2] = clamp(b + clamp(random_value[2]))

    cv.imshow("Gaussian image", image)


src = cv.imread("./images/flowers01.jpg")
cv.imshow("原图", src)

# 统计时间
# getTickCount()函数返回操作系统启动到当前所经过的计时周期数
t1 = cv.getTickCount()
Gaussian_noise(src)
t2 = cv.getTickCount()
# getTickFrequency()函数，返回CPU的频率
time = (t2 - t1)/cv.getTickFrequency()
print("耗费时间：%s"%time)  # 耗费时间：10.2369628

# GaussianBlur(src, ksize, sigmaX, dst=None, sigmaY=None, borderType=None)
dst = cv.GaussianBlur(src, (0, 0), 15)
cv.imshow("Gaussian image 2", dst)
cv.waitKey(0)
cv.destroyAllWindows()