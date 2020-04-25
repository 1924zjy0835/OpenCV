
import cv2 as cv
from matplotlib import pyplot as plt


def plot_demo(image):
    # numpy中的ravel()/flatten()/squeeze()都有将多维数组转换为一维数组的功能
    plt.hist(image.ravel(), 256, [0,256])
    plt.show()


def image_hist(image):
    color = ("blue", "green", "red")
    for i, color in enumerate(color):
        hist = cv.calcHist([image], [i], None, [256], [0,256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    plt.show()


src = cv.imread("./images/raindropGirl.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
plot_demo(src)
# image_hist(src)
cv.waitKey(0)
cv.destroyAllWindows()