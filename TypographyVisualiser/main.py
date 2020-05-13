import os
import sys
import requests
import subprocess
import pkg_resources

from flask import Flask, render_template

# importiere jedes Modul, das der Nutzer nicht hat, wir aber benötigen
required = {'bs4', 'flask'}
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

SAVE_FOLDER = "images"

##############################################

app = Flask(__name__)


@app.route('/')
def start():
    return "<h2>This is a Test</h2>"


@app.route('/home')
def home():
    return "Homepage"

def search():
    from bs4 import BeautifulSoup

    query = input("Nach was möchtest du suchen? : ")

    # Such nach dem eingegebenen Begriff
    searchurl = GOOGLE_IMAGE_URL + 'q=' + query

    response = requests.get(searchurl, headers=USR_AGENT)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    results = soup.findAll('img', {'class': 't0fcAb'}, limit=5)


    imageLinks = []
    for result in results:
        seperates = str(result).split(' ')
        parts = seperates[3].split('"')
        imageLinks.append(parts[1])

    for link in imageLinks:
        print(link)


    # Erstelle einen Ordner, in den Bilder heruntergeladen werden
    if not os.path.exists(SAVE_FOLDER):
        os.mkdir(SAVE_FOLDER)

    # Alle Links gefiltert -> Runterladen
    for i, imageLink in enumerate(imageLinks):
        response = requests.get(imageLink)

        imageName = SAVE_FOLDER + '/' + query + str(i+1) + '.jpg'
        with open(imageName, 'wb') as file:
            file.write(response.content)


if __name__ == "__main__":
    # app.run(debug=True)
    search()