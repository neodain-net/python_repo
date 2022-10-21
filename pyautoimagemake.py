from PIL import Image, ImageDraw, ImageFont, ImageFilter

print("Image File open")
img = Image.open("../images/white_pannel.png")

width, height = img.size
print(f"Image Size : {width} x {height}")

# 그림판에 이미지를 가져오기
draw = ImageDraw.Draw(img)

# text = "너는 이루어 낼거야~ 2000억 벌기 !!!"
text = "7"
# 삽입할 문자의 폰트 설정
font = ImageFont.truetype(
    r"C:\Users\neo\Downloads\nanum-all\나눔 글꼴\나눔바른고딕\NanumBarunGothic.ttf", 100
)

width_txt, height_txt = draw.textsize(text, font)
print(f"Text Size : {width_txt} x {height_txt}")

margin = 10
x = width - width_txt - margin
y = height - height_txt - margin

print(f"Text start position : {x} x {y}")

# 삽입할 문자 text 적용하기
# draw.text((x, y), text, fill='white', font=font)
draw.text((x, y), text, fill="black", font=font)

area = (x, y, x + 70, y + 100)

crop_image = img.crop(area)

# 이미지 출력
crop_image.show()

# 작업한 이미지 저장
# img.save("cat_watermark.png")
crop_image.save("../images/7.png")
print("image job end")

img.close()


import os
import openpyxl as op
from openpyxl.drawing.image import Image
from PIL import Image as pi


def resizeImg(size, img_path, img_name):
    img = pi.open(img_path + "/" + img_name)
    resize_img = img.resize(size)
    # resize_img.save(img_path+"/"+img_name, "JPEG", quality=95)
    resize_img.save(img_path + "/" + img_name, "PNG", quality=95)
    img.close()


def insertImg(file_path, img_path, img_name, save_path):
    file_list = os.listdir(file_path)
    for file in file_list:
        print(f"file list : {file}")
        wb = op.load_workbook(file_path + "/" + file)
        ws = wb.active
        img = Image(img_path + "/" + img_name)
        ws.add_image(img, "A1")
        wb.save(save_path + "/" + file)


if __name__ == "__main__":
    file_path = r"C:\Users\neo\work\python_win\excel"
    image_path = r"C:\Users\neo\work\python_win\image"
    save_path = r"C:\Users\neo\work\python_win\save"
    # image_name = "cat_watermark.png"
    # size = (500,200)
    # print(f"resize[500,200] image file name : {image_name}")
    # resizeImg(size, image_path, image_name)
    # insertImg(file_path, image_path, image_name, save_path)
