# @Description: videoCapture.py
# @Author: 孤烟逐云zjy
# @Date: 2020/4/20 11:15
# @SoftWare: PyCharm
# @CSDN: https://blog.csdn.net/zjy123078_zjy
# @博客园: https://www.cnblogs.com/guyan-2020/

import cv2 as cv
import numpy as np


"""
def video_capture_demo():
    # 使用cv2.VideoCapture()创建一个VideoCapture对象
    video = cv.VideoCapture("./dist/video/WeChat_20200420111942.mp4")
    while(True):
        # 读取视频的每一帧，如果可以正常读取的话，就返回True，否者的话，就返回False，并且退出程序
        ret, frame = video.read()
        if ret == False:
            break
        video_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        lower_hsv = np.array([26, 0, 0])
        upper_hsv = np.array([60, 255, 255])

        # cv.inRange(src, lowerb, upperb, dst) src:输入的原视频文件，lowerb：HSV色彩空间的低值，upperb：HSV色彩空间的高值，dst: 输出图像
        # cv2.inRange()，可以对单通道或多通道操作
        mask = cv.inRange(video_hsv, lowerb=lower_hsv, upperb=upper_hsv)
        dst = cv.bitwise_and(frame, frame, mask=mask)
        cv.imshow("video", frame)
        cv.imshow("mask video", dst)
        c = cv.waitKey(40)
        if c == 27:
            break


video_capture_demo()
cv.waitKey(0)
cv.destroyAllWindows()
"""


"""
# 获取图片
def image_capture_demo():
    image = cv.imread("./images/flowers01.jpg")
    image_hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    lower_hsv = np.array([0, 1, 46])
    upper_hsv = np.array([40, 255, 255])
    image_mask = cv.inRange(image_hsv, lowerb=lower_hsv, upperb=upper_hsv)
    dst_image = cv.bitwise_and(image, image, mask=image_mask)
    not_image = cv.bitwise_not(image)
    cv.imshow("mask image:", dst_image)
    cv.imshow("Not image demo",not_image)
    cv.waitKey(0)
    cv.destroyAllWindows()


image_capture_demo()
cv.waitKey(0)
cv.destroyAllWindows()
"""


"""
video_capture_demo()
src = cv.imread("./images/photo01.jpg")

# 将每一个通道进行拆分
b, g, r = cv.split(src)

cv.imshow("blue image", b)
cv.imshow("red image", r)
cv.imshow("green image", g)

# 为某一个通道的赋值
src = cv.merge([b, g, r])
src[:, :, 1] = 0
cv.imshow("changed image", src)

cv.waitKey(0)
cv.destroyAllWindows()
"""

