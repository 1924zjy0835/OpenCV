# @Description: Person.py
# @Author: 孤烟逐云zjy
# @Date: 2020/4/23 15:27
# @SoftWare: PyCharm
# @CSDN: https://blog.csdn.net/zjy123078_zjy
# @博客园: https://www.cnblogs.com/guyan-2020/

import cv2 as cv
import numpy as np


def is_inside(o, i):
    ox, oy, ow, oh = o
    ix, iy, iw, ih = i
    return ox > ix and oy > iy and ox + ow < ix + iw and oy + oh < iy+ ih


def draw_person(image, person):
    x, y, w, h = person
    cv.rectangle(image, (x, y), (x + w, y + h), (255, 0, 255), 2)


img = cv.imread("./images/peopleMore01.jpg")
hog = cv.HOGDescriptor()
hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())

found, w = hog.detectMultiScale(img)

found_filtered = []
for ri, r in enumerate(found):
    for qi, q, in enumerate(found):
        if ri != qi and is_inside(r, q):
            break
        else:
            found_filtered.append(r)
    for person in found_filtered:
        draw_person(img, person)

cv.imshow("people detection", img)
cv.waitKey(0)
cv.destroyAllWindows()