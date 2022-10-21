from tkinter import *
import torch
from PIL import Image, ImageTk


def read_square_image(filename, size):
    img = Image.open(filename).convert("RGB")

    w, h = img.size

    if w > h:
        d = (w - h) // 2
        img = img.crop((d, 0, h + d, h))
    else:
        d = (h - w) // 2
        img = img.crop((0, d, w, w + d))

    return img.resize((size, size), Image.ANTIALIAS)


def cartoonify(img, pretrained, size):
    model = torch.hub.load(
        "bryandlee/animegan2-pytorch:main", "generator", pretrained=pretrained
    )
    face2paint = torch.hub.load(
        "bryandlee/animegan2-pytorch:main", "face2paint", size=size
    )
    return face2paint(model, img)


img = read_square_image("../images/my_photo_02.png", 256)

img = cartoonify(img, "paprika", 256)

img.show()


# img.show()

# canvas / label / button 만들어 보기
window = Tk()

img_tk = ImageTk.PhotoImage(img)

canvas_test = False
if canvas_test:
    canvas = Canvas(window, bg="white", width=128, height=128)
    canvas.create_image(0, 0, anchor=NW, image=img_tk)  # 다른 이미지로 교체할 때도 사용

    label = Label(window, image=img_tk)
    # label["image"] = img_tk # 다른 이미지로 교체도 가능

    button = Button(window, image=img_tk)

    canvas.pack(side=LEFT)
    label.pack(side=LEFT)
    button.pack(side=LEFT)

# 레이블과 버튼을 프레임으로 묶기
frame1 = Frame(window)
frame2 = Frame(window)

label1 = Label(frame1, text="Frame1")
button1 = Button(frame1, image=img_tk)

label1.pack(side=TOP)
button1.pack(side=TOP)

label2 = Label(frame2, text="Frame2")
button2 = Button(frame2, image=img_tk)

label2.pack(side=TOP)
button2.pack(side=TOP)

frame1.pack(side=LEFT)
frame2.pack(side=LEFT)

window.mainloop()
