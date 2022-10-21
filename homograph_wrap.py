import cv2
import numpy as np


def virtual_billboard(im_src, im_dst):
    pts_src = np.array([[2, 2], [1917, 4], [1916, 1012], [2, 1008]])
    pts_dst = np.array([[421, 205], [1510, 137], [1502, 676], [415, 642]])

    h, status = cv2.findHomography(pts_src, pts_dst)
    print(h.shape)  # (3, 3) matrix

    im_wrap = cv2.warpPerspective(im_src, h, (im_dst.shape[1], im_dst.shape[0]))

    cv2.fillConvexPoly(im_dst, pts_dst.astype(int), (0, 0, 0), cv2.LINE_AA)

    return im_wrap + im_dst


im_src = cv2.imread("../images/capture/src00000.jpg")
im_dst = cv2.imread("../images/capture/dest00000.jpg")

im_comp = virtual_billboard(im_src, im_dst)

cv2.imshow("Warped Source Image", im_comp)

cv2.waitKey(0)
cv2.destroyAllWindows()
