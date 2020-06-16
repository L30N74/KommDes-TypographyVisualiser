import os
import cv2
from flask import Blueprint, request, json

contourCreator = Blueprint("contourCreator", __name__, static_folder="static")


@contourCreator.route("/Contours", methods=['POST'])
def getContours():
    thresh_low = int(request.form.get('thresh_low'))
    thresh_high = int(request.form.get('thresh_high'))

    if thresh_low is None: return
    if thresh_high is None: return

    # import image(s)
    images = []
    imagePath = "static/images/"
    outputPath = "static/output/"
    imageIndex = 0
    for image in os.listdir(imagePath):

        loaded_image = cv2.imread(imagePath + image)
        image_gray = cv2.cvtColor(loaded_image, cv2.COLOR_BGR2GRAY)

        edged = cv2.Canny(image_gray, thresh_low, thresh_high, edges=True)

        contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        filename = f'static/output/result-{str(imageIndex)}.jpg'
        cv2.imwrite(filename, edged)
        images.append(filename)
        imageIndex += 1

    return json.dumps(images)
