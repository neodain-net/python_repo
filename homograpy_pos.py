import numpy as np
import cv2 as cv


def check_xy(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print(f"[{x}, {y}],", end="")


img = cv.imread("images/capture/src00000.jpg")

cv.namedWindow("Image")
cv.setMouseCallback("Image", check_xy)

while True:
    cv.imshow("Image", img)

    if cv.waitKey(20) & 0xFF == ord("q"):
        break

cv.destroyAllWindows()
