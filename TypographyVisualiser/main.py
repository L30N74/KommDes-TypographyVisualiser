from flask import Flask, render_template

from imageDownloader import imageDownloader
from contourCreator import contourCreator

##############################################

app = Flask(__name__)
app.register_blueprint(imageDownloader)
app.register_blueprint(contourCreator)


@app.route('/')
@app.route('/Start')
def start():
    return render_template('step1.html')  # Nimm das Dokument home.html aus Ordner templates


@app.route('/Settings')
def settings():
    return render_template('settings.html')


if __name__ == "__main__":
    app.run(debug=True)
