import cv2, glob
import numpy as np
import ffmpeg


def virtual_billboard(im_src, im_dst):
    pts_src = np.array([[2, 2], [1917, 4], [1916, 1012], [2, 1008]])
    pts_dst = np.array([[421, 205], [1510, 137], [1502, 676], [415, 642]])

    h, status = cv2.findHomography(pts_src, pts_dst)
    # print(h.shape)  # (3, 3) matrix

    im_wrap = cv2.warpPerspective(im_src, h, (im_dst.shape[1], im_dst.shape[0]))

    cv2.fillConvexPoly(im_dst, pts_dst.astype(int), (0, 0, 0), cv2.LINE_AA)

    return im_wrap + im_dst


print(f'src file num  : {len(glob.glob("../images/capture/src*.jpg"))}')
print(f'dest file num : {len(glob.glob("../images/capture/dest*.jpg"))}')

file_num = min(
    len(glob.glob("../images/capture/dest*.jpg")),
    len(glob.glob("../images/capture/dest*.jpg")),
)
print(f"selected file num : {file_num}")

for i in range(file_num):
    im_src = cv2.imread("../images/capture/src" + str(i).zfill(5) + ".jpg")
    im_dst = cv2.imread("../images/capture/dest" + str(i).zfill(5) + ".jpg")

    im_comp = virtual_billboard(im_src, im_dst)

    cv2.imwrite("../images/capture/comp" + str(i).zfill(5) + ".jpg", im_comp)

# 이미지 시퀀스를 동영상으로 묶기
ffmpeg.input("../images/capture/comp%5d.jpg").output(
    "../images/virtual_concert.mp4", start_number=0
).run(capture_stdout=True, capture_stderr=True)

# audio 추출하기
ffmpeg.input("../images/bts_dynamite.mp4").output("../images/bts_dynamite.wav").run()

# video / audio 합치기
video = ffmpeg.input("../images/virtual_concert.mp4").video  # get only video channel
audio = ffmpeg.input("../images/bts_dynamite.wav").audio  # get only video channel

output = ffmpeg.output(
    video,
    audio,
    "../images/virtual_concert_comp.mp4",
    vcodec="copy",
    acodec="aac",
    strict="experimental",
)

ffmpeg.run(output)
