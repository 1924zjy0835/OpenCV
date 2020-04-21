# @Description: color_space.py
# @Author: 孤烟逐云zjy
# @Date: 2020/4/20 7:12
# @SoftWare: PyCharm
# @CSDN: https://blog.csdn.net/zjy123078_zjy
# @博客园: https://www.cnblogs.com/guyan-2020/


import cv2 as cv


# 读取本地图片
# def image_read():

# HSV格式中H（色彩/色度）的取值范围是[0, 179]，S（饱和度）的取值范围是[0,255]中，V（亮度）的取值范围是[0,255]。
# 不同的软件的HSV值可能不同，要进归一化处理


# 色彩空间转换
def color_space_demo(image):
    # cv.cvtColor(input_image, flag) flag指的是要转换的类型
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # 从BGR到灰度图使用到的flag就是cv2.COLOR_BGR2GRAY
    cv.imshow("gray image", gray)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)    # 从BGR到HSV,使用到的flag就是cv2.COLOR_BGR2HSV

    # 可以使用下面的命令获取所有的可用的flag
    # flags = [i for in dir(cv) if i startswith("COLOR_")]
    # print(flags)

    cv.imshow("hsv image", hsv)
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    cv.imshow("yuv image", yuv)
    Ycrcb = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)
    cv.imshow("ycrcb image", Ycrcb)


image = cv.imread("./images/photo01.jpg")
# cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("show image", image)

# color_space_demo(image)

cv.waitKey(0)
cv.destroyAllWindows()


