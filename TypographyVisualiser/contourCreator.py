import cv2
from flask import Blueprint, request

contourCreator = Blueprint("contourCreator", __name__, static_folder="static")


@contourCreator.route("/Contours", methods=['POST'])
def getContours():
    print("---------------------- Contours")
    imagePath = str(request.form.get('imagePath'))
    thresh_low = int(request.form.get('thresh_low'))
    thresh_high = int(request.form.get('thresh_high'))


    # import image
    image = cv2.imread(imagePath)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    edged = cv2.Canny(image_gray, thresh_low, thresh_high, edges=True)

    contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.imwrite("static/output/result.jpg", edged)

    return "Nothing"