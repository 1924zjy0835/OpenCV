import cv2 as cv
import numpy as np


# 遍历读取图片的每一个像素点，打印出其属性值
# def access_pixels(image):
    # print(image.shape)
    # height = image.shape[0]
    # width = image.shape[1]
    # channels = image.shape[2]
    # print("width:%s,height:%s,channels:%s"% (width,height,channels))


    # 遍历每一个像素点，并且修改一个像素点的值。
    # for row in range(height):
    #     for col in range(width):
    #         for c in range(channels):
    #             pv = image[row,col,c]
    #             image[row,col,c] = 255 - pv
    # cv.imshow("P1",image)

# 当前所用的时间为：458.1146 ms

# 上面的操作就是对像素点进行取反操作。
# 另外就是Open CV定义了专门的API->bitwise_not()函数进行对像素点进行取反操作
# 因为Open CV是用C语言来写的。所以，在运算起来的时候就是比较快的
# 所以在运用的时候，我们就要更加高效率的使用Open CV内置的函数，可以提高效率
def inverse(image):
    dst = cv.bitwise_not(image)
    cv.imshow("Inverse Windows06",dst)
# # 运行速度：当前所用的时间为：32.9174 ms


# 创建一张图片，定义图片的大小以及dtype类型
def create_image():

    # 创建一个多通道的8位图像进行显示，
    # 修改图片的像素点的值
    # 创建一个三通道的长宽为400，并且dtype类型为np.uint8
    img = np.zeros([400,400,3],np.uint8)

#     但是我们同样可以对创建的图片的每一个像素点进行修改，
#     对第一个通道的像素点进行修改，
    img[:,:,0] = np.ones([400,400])*255

#     此时就已经可以进行显示了
    cv.imshow('Image Windows02',img)


    #  2.创建一个单通道8位的图像进行显示
    # 在这里我们学到了怎么初始化图像，
    # 一种是可以将图像得每一个的像素点都变成0
    # 另外一种就是将所有的像素点都变成1，并且可以进行乘法改变像素的大小
    # 单通道的一定也要加上通道数1,要不然会认为是二维的。
    # 并且会报错，IndexError: too many indices for array

    # 1. 初始化的时候，使用0,进行初始化
    # img = np.zeros([400,400,1],np.uint8)
    # # 127就是灰度图像
    # img[:, :, 0] = np.ones([400,400])*127

    # 2. 初始化的时候使用1进行初始化，会更加灵活一点
    img = np.ones([400, 400, 1], np.uint8)

    # 得到的是灰度图像
    img1 = img*127

    # 得到的是黑色图像
    img2 = img*0

    # 显示图像
    cv.imshow("Image Windows04",img1)
    cv.imshow("Image Windows05",img2)

    # 保存图像到本地dist/images/turtor_01/img_127.jpg和img_0.jpg
    cv.imwrite('./dist/images/turtor_01/img_127.jpg',img1)
    cv.imwrite('./dist/images/turtor_01/img_0.jpg',img2)

    # cv.imshow("Image windows03",img)


    # 3. 初始化一个多维数组,在以后进行图像处理时，如果有浮点型的，一定要用浮点型
    # 避免数据被截断
    m1 = np.ones([3,3],np.float)
    m1.fill(12.33)
    print(m1)

#     使用reshape()函数进行转换数组的维度
#     reshape()函数只是改变的数据的表示形式，但是并不会改变数据
    m2 = m1.reshape([1,9])
    print(m2)

print("----------- Hello Guyan -----------")
src = cv.imread('./images/handsomeboy01.jpg')
cv.namedWindow("Image Windows01",cv.WINDOW_AUTOSIZE)
cv.imshow("Image Windows01",src)

# getTickCount()返回从操作F系统启动到当前所经过的计时周期数
t1 = cv.getTickCount()
# access_pixels(src)
# getTickCount()函数，返回从操作系统启动到当前的计时周期数

# 此时就只是调用自己创建图片的函数create_image()
# create_image()
inverse(src)

t2 = cv.getTickCount()
# getTickFrequency()函数，用于返回CPU的频率，
# (getTickCount1 - getTickCount2)/getTickFrequency():
# (当前次数 - 开始计时次数) / 每秒钟重复次数 = 等于从开始到当前所用的时间。
time = (t2 - t1) / cv.getTickFrequency()

# 注意这里一定要带上括号，要不然就会将当前是所用的时间打印1000次
# print('当前所用的时间为：%s ms' % time*1000)
print('当前所用的时间为：%s ms' % (time*1000))
cv.waitKey(0)
cv.destroyAllWindows()