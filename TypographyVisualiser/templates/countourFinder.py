import PIL
import numpy as np

from PIL import Image, ImageFont, ImageDraw

image_path = "../static/output/result-0.jpg"
font_type = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 5)
searchterm = "duck"
color = (255, 69, 0)


def read_image(path):
    try:
        img = PIL.Image.open(path)
        return img
    except Exception as e:
        print(e)


image = read_image(image_path)
# image.show()

img_array = np.array(image)

# np.set_printoptions(threshold=np.inf)
print(img_array)
y = 0
x = 0
draw = ImageDraw.Draw(image)
for line in img_array:

    for p in line:

        if p >= 250:
            # print(p)
            # draw = ImageDraw.Draw(image)
            draw.text(xy=(x, y), text=searchterm, fill=145, font=font_type)



        else:
            print("nope")
        print(x)

        x = x + 1


    print(y)
    y = y + 1
    x = 0

image.show()



