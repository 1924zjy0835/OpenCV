# @Description: ROI.py
# @Author: 孤烟逐云zjy
# @Date: 2020/4/22 10:53
# @SoftWare: PyCharm
# @CSDN: https://blog.csdn.net/zjy123078_zjy
# @博客园: https://www.cnblogs.com/guyan-2020/

import cv2 as cv
import numpy as np

src1 = cv.imread("./images/photo02.jpg")

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


cv.waitKey(0)
cv.destroyAllWindows()