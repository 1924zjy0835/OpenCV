import cv2 as cv

# cv模块下的imread()函数可以读出图片
# 将读出的图像付给一个新的变量
src = cv.imread("images/handsomeboy01.jpg")

# 有了图片之后，我们就可以创建一个GUI将它显示出来。
# 通过Open CV框架进行创建这个显示图像的窗口
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)

# 通过函数imshow()进行显示图像在当前的窗口，
# 但是这个显示的窗口怎么和之前创建的窗口进行吻合呢？
# 这时就可以通过名字与之前的窗口进行吻合。
cv.imshow("input image",src)

# Open CV在创建一个窗口之后，如果没有告诉它多久关掉的话，
# 它就会等到你的下一次操作执行的时候，进行关掉。
cv.waitKey(0)
cv.destroyAllWindows()
# 等到用户的下次操作时，它就会关闭窗口，并且释放掉所有的内存。
