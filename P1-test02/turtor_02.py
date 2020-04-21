
# 读取视频


import cv2 as cv


def video_demo():
    # 打开电脑上的USB摄像头
    capture = cv.VideoCapture(0)
    # 打开摄像头之后就可以进行读写操作了
    while(True):
        # 读视频的时候会返回两个值，一个是return，即为返回值；
        ret,frame = capture.read()
        # 将视频显示的时候进行左右变换，并且输出。同样也可以上下变换
        frame = cv.flip(frame,1)
        # frame即为读取的视频的每一帧，之后就会将视频的每一帧显示出来
        cv.imshow("Video Image",frame)
        # 定义用户50ms之后进行关闭窗口
        c = cv.waitKey(50)
        if c == 27:
            break


video_demo()
cv.imshow(0)
# 关闭窗口，只需要告诉它窗口的名字就可以了。
cv.destroyAllWindows()


