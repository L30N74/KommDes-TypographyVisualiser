import os
import sys
import cv2
import numpy
import urllib.request
from matplotlib import pyplot
import requests
import subprocess
import pkg_resources
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, url_for, jsonify

# importiere jedes Modul, das der Nutzer nicht hat, wir aber benötigen
required = {'bs4', 'opencv-python', 'flask'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    python = sys.executable

    # Rufe für jedes fehlende Modul "pip install <Modul>" auf
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

##############################################

# Globales
GOOGLE_IMAGE_URL = \
    'https://www.google.de/search?site=&tbm=isch&'

USR_AGENT = {
    'User-Agent': 'My User Agent 1.0',
}

##############################################

app = Flask(__name__)

images = []


@app.route('/')
def start():
    return render_template('step1.html')  # Nimm das Dokument home.html aus Ordner templates


@app.route('/DownloadImages', methods=['POST', 'GET'])
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


@app.route('/Settings')
def settings():
    return render_template('step2.html')


@app.route("/Contours", methods=['POST'])
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
    # cv2.imshow("canny edges", edged)
    # cv2.waitKey(0)

    return "Nothing"


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


def imageToGrayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


if __name__ == "__main__":
    app.run(debug=True)
