# @Description: ROI.py
# @Author: 孤烟逐云zjy
# @Date: 2020/4/22 10:53
# @SoftWare: PyCharm
# @CSDN: https://blog.csdn.net/zjy123078_zjy
# @博客园: https://www.cnblogs.com/guyan-2020/

import cv2 as cv
import numpy as np

src1 = cv.imread("./images/photo02.jpg")

"""
def fill_color_demo(image):
    copyImage = image.copy()
    h, w = image.shape[:2]
    mask = np.zeros([h+2, w+2], np.uint8)
    cv.floodFill(copyImage, mask, (30, 30), (0, 255, 255), (100, 100, 100), (50, 50, 50), cv.FLOODFILL_FIXED_RANGE)
    cv.imshow("fill color demo", copyImage)
    cv.imshow(" color demo", image)
    # print("h: %s, w:%s"%(h, w))


fill_color_demo(src1)
"""


# 颜色二值填充
def fill_binary():
    image = np.zeros([400, 400, 3], np.uint8)
    image[100:300, 100:300, : ] = 255

    mask = np.ones([402, 402, 1], np.uint8)
    mask[201:301, 101:301] = 0
    # cv.imshow("mask binary", mask)   # 黑色
    # ROI区域的选择，开始点的选择
    # floodFill(image, mask, seedPoint, newVal, loDiff=None, upDiff=None, flags=None)
    # src(seed.x, seed.y)-loDiff <= src(x,y) <=src(seed.x, seed.y)+upDiff
    # 泛洪填充，如何填充一个对象内部区域
    # 1.FLOODFILL_FIXED_RANGE: 改变图像，泛洪填充
    # 2.FLOODFILL_MASK_ONLY: 不改变图像，只填充遮罩层本身，忽略新的颜色值参数
    cv.floodFill(image, mask, (200, 200), (0, 255, 255), cv.FLOODFILL_MASK_ONLY)
    cv.imshow("binary image", image)


fill_binary()


"""
src2 = cv.imread("./images/flowers01.jpg")
src1_cpy = src1.copy()
src2_cpy = src2.copy()
flower = src2_cpy[100:400, 200:500]
person = src1_cpy[100:400, 200:500]
flower_gray = cv.cvtColor(flower, cv.COLOR_BGR2GRAY)
flower_BGR = cv.cvtColor(flower_gray, cv.COLOR_GRAY2BGR)

src1_cpy[150:450, :300] = flower_BGR
cv.imshow("flower image", flower)
cv.imshow("person image", person)
cv.imshow("src1_cpy image", src1_cpy)
"""

cv.waitKey(0)
cv.destroyAllWindows()