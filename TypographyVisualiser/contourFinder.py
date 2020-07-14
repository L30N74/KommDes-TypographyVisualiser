import PIL
import cv2
import numpy as np

from PIL import Image, ImageFont, ImageDraw
from flask import Blueprint, request, json


contourFinder = Blueprint("contourFinder", __name__, static_folder="static")


@contourFinder.route("/Outline", methods=['POST'])
def draw_outline():

    image_path = "static/output/result-0.jpg"
    font_type = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 15)
    searchterm = "duck"
    color = (255, 69, 0)

    image = read_image(image_path)
    # image.show()

    img_array = np.array(image)

    # np.set_printoptions(threshold=np.inf)
    print(img_array)
    y = 0
    x = 0
    i = 0
    draw = ImageDraw.Draw(image)

    for line in img_array:

        for p in line:

            if p >= 250:
                # print(p)
                # draw = ImageDraw.Draw(image)

                if i % 10 == 0:
                    draw.text(xy=(x, y), text=searchterm, fill=230, font=font_type)
                i = i + 1
                p = 0

            else:
                print("nope")
            print(x)

            x = x + 1

        print(y)
        y = y + 1
        x = 0

    # image.show()
    image.save(image_path)

    return "Nothing"


@contourFinder.route("/Fill", methods=['POST'])
def fill_outline():
    pass


def read_image(path):
    try:
        # img = PIL.Image.open(path)

        size = 1280, 720
        img = Image.open(path)
        img_resized = img.resize(size, Image.ANTIALIAS)
        return img_resized
    except Exception as e:
        print(e)



