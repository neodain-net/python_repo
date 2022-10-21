import os, os.path
import ffmpeg

# scriptpath = os.path.dirname(__file__)
# print(f"__file__ : {__file__}, scriptpath = {scriptpath}")
# video_src = os.path.join(scriptpath, r"../images/my_girl.mp4")
# print(f"video_src = {video_src}")
# if not os.path.isdir(r"../images/capture"):
#     os.mkdir(r"../images/capture")
# else:
#     print('already "../images/capture" directory exist')

# try:
#     ffmpeg.input("../images/NO_FILE.mp4").output("../images/capture/dest%05d.jpg", start_number=0).run(capture_stdout=True, capture_stderr=True)
# except ffmpeg.Error as e:
#     print('stdout:', e.stdout.decode('utf8'))
#     print('stderr:', e.stderr.decode('utf8'))

ffmpeg.input("../images/bts_dynamite.mp4").output(
    "../images/capture/dest%05d.jpg", start_number=0
).run(capture_stdout=True, capture_stderr=True)

ffmpeg.input("../images/my_face.mp4").output(
    "../images/capture/src%05d.jpg", start_number=0
).run(capture_stdout=True, capture_stderr=True)

# print(os.listdir("../images/capture"))

import glob

print(f'src file num  : {len(glob.glob("../images/capture/src*.jpg"))}')
print(f'dest file num : {len(glob.glob("../images/capture/dest*.jpg"))}')

file_num = min(
    len(glob.glob("../images/capture/dest*.jpg")),
    len(glob.glob("../images/capture/dest*.jpg")),
)
print(f"selected file num : {file_num}")
