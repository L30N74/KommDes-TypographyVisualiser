import os
import cv2
import urllib
import numpy
import requests
from bs4 import BeautifulSoup
from flask import Blueprint, request, jsonify

imageDownloader = Blueprint("imageDownloader", __name__, static_folder="static")

# Globales
GOOGLE_IMAGE_URL = \
    'https://www.google.de/search?site=&tbm=isch&'

USR_AGENT = {
    'User-Agent': 'My User Agent 1.0',
}

images = []


@imageDownloader.route('/DownloadImages', methods=['POST'])
def search():
    keyword = str(request.form.get('keyword'))
    image_amount = int(request.form.get('amount'))
    color = str(request.form.get('color'))

    if keyword is None or image_amount is None:
        return None

    # Such nach dem eingegebenen Begriff
    searchurl = GOOGLE_IMAGE_URL + 'q=' + keyword

    response = requests.get(searchurl, headers=USR_AGENT)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    download(keyword, soup, image_amount)

    # Angabe der Anzahl der runtergeladenen Bilder macht Suche einfacher
    return jsonify({"amount": len(images)})


def download(searchQuery, html, imageAmount):
    results = html.findAll('img', {'class': 't0fcAb'}, limit=imageAmount)

    imageLinks = []
    for result in results:
        seperates = str(result).split(' ')
        parts = seperates[3].split('"')
        imageLinks.append(parts[1])

    imageFolder = "static/images/" + searchQuery
    if not os.path.exists(imageFolder):
        os.mkdir(imageFolder)

    # Download image
    for url in imageLinks:
        # Anzahl an Bildern in Ordner, um Bilder zu benennen (image-0 bis image-n)
        imageIndex = len([name for name in os.listdir(imageFolder) if os.path.isfile((os.path.join(imageFolder, name)))])

        # Bild runterladen
        newImage = cv2.imwrite("{0}/{1}-{2}.jpg".format(imageFolder, searchQuery, imageIndex), urlToImage(url))
        images.append(newImage)


def urlToImage(url):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    resp = urllib.request.urlopen(url)
    image = numpy.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    # return the image
    return image
