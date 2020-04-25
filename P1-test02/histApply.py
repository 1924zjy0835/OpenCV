# @Description: histApply.py
# @Author: 孤烟逐云zjy
# @Date: 2020/4/24 12:55
# @SoftWare: PyCharm
# @CSDN: https://blog.csdn.net/zjy123078_zjy
# @博客园: https://www.cnblogs.com/guyan-2020/

import cv2 as cv
import numpy as np

src = cv.imread("./images/handsomeboy01.jpg")


# 1. 全局直方图均衡化
def globalEqualHist(image):
    # 如果想要对图片做均衡化，必须将图片转换为灰度图像
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    dst = cv.equalizeHist(gray)  # 在说明文档中有相关的注释与例子
    # equalizeHist(src, dst=None)函数只能处理单通道的数据,src为输入图像对象矩阵，必须为单通道的uint8类型的矩阵数据
    # dst: 输出图像矩阵(src的shape一样)
    cv.imshow("global equalizeHist", dst)
    # print(len(image.shape))  # 彩色图像的shape长度为3
    # print(len(gray.shape))  # 灰度图像的shape长度为2
    # print(gray.shape)   # 灰度图像只有高、宽


# 2. 局部直方图自适应均衡化
# 相比全局直方图均衡化，自适应直方图均衡化将图像划分为不重叠的小块，在每一块进行直方图均衡化，
# 如果小块内有噪声，则影响就会很大，需要通过限制对比度来进行抑制。即通过对比度自适应直方图均衡化。如果限制对比度的阈值设置为40，
# 那么在图像中像素值出现次数大于40的次数就会将大于40的部分像素点去掉，平均成其它的像素点。
def localEqualHist(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    clahe = cv.createCLAHE(clipLimit=5, tileGridSize=(7,7))
    dst = clahe.apply(gray)
    cv.imshow("clahe image", dst)


# 直方图比较
def create_rgb_hist(image):
    h, w, c = image.shape
    rgbHist = np.zeros([16*16*16, 1], np.float32)
    bsize = 256/16
    # enumerate() 函数可以永健一个可遍历的数据对象（如列表、元组或字符串）组合为一个索引序列，同时列出数据以及对应的下标，一般用在for循环中。
    # range()函数用于创建一个整数列表
    for row in range(h):
        for col in range(w):
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            index = np.int((b/bsize)/16*16 + (g/bsize)*16 + (r/bsize))
            rgbHist[np.int(index), 0] = rgbHist[np.int(index), 0] + 1

    return rgbHist


def hist_compare(image1, image2):
    hist1 = create_rgb_hist(image1)
    hist2 = create_rgb_hist(image2)
    match1 = cv.compareHist(hist1, hist2, cv.HISTCMP_BHATTACHARYYA)
    match2 = cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
    match3 = cv.compareHist(hist1, hist2, cv.HISTCMP_CHISQR)
    print("巴氏距离: %s, 相关性: %s, 卡方: %s"%(match1, match2, match3))
    cv.imshow("image1", image1)
    cv.imshow("image2", image2)


image1 = cv.imread("./images/raindropGirl.jpg")
image2 = cv.imread("./images/raindropGirl01.jpg")

hist_compare(image1, image2)
# cv.imshow("original image", src)
cv.waitKey(0)
cv.destroyAllWindows()