import numpy as np

from PIL import Image, ImageFont, ImageDraw
from flask import Blueprint, request
import matplotlib

contourFinder = Blueprint("contourFinder", __name__, static_folder="static")


@contourFinder.route("/Outline", methods=['POST'])
def draw_outline():
    image_path = "static/output/result-0.jpg"
    background_image_path = "static/output/final-result-0.jpg"
    font_type = ImageFont.truetype('fonts/Roboto-Light.ttf', 20)
    search_term = str(request.form.get('keyword'))
    color = str(request.form.get('color'))

    image_template = Image.open(image_path)
    image_template = resize_image(image_template)
    # preparation for final-result background 
    create_background_image()
    background_image = Image.open(background_image_path)
    #
    image_template_array = np.array(image_template)

    # draw on background image
    draw = ImageDraw.Draw(background_image)
    y = 0
    x = 0
    i = 0

    for line in image_template_array:

        for pixel in line:

            if pixel >= 250:
                # print(p)
                # draw = ImageDraw.Draw(image)

                if i % 10 == 0:
                    draw.text(xy=(x, y), text=search_term, fill=color, font=font_type)
                i = i + 1
                pixel = 0

            # else:
            # print("nope")
            # print(x)

            x = x + 1

        # print(y)
        y = y + 1
        x = 0

    background_image.save(background_image_path)

    return "Nothing"


@contourFinder.route("/Fill", methods=['POST'])
def fill_outline():
    pass


def resize_image(img):
    try:
        size = 1920, 1080
        img_resized = img.resize(size, Image.ANTIALIAS)
        return img_resized
    except Exception as e:
        print(e)


def create_background_image():
    try:
        background_image_array = np.zeros((1080, 1920))
        matplotlib.image.imsave('static/output/final-result-0.jpg', background_image_array)
        print("background finish")
    except Exception as e:
        print(e)
