from flask import Flask, render_template

from imageDownloader import imageDownloader
from contourCreator import contourCreator
from contourFinder import contourFinder

##############################################

app = Flask(__name__)
app.register_blueprint(imageDownloader)
app.register_blueprint(contourCreator)
app.register_blueprint(contourFinder)


@app.route('/')
@app.route('/Start')
def start():
    return render_template('step1.html')  # Nimm das Dokument home.html aus Ordner templates


@app.route('/Settings')
def settings():
    return render_template('step2.html')


@app.route('/Finish')
def finish():
    return render_template('step3.html')


if __name__ == "__main__":
    app.run(debug=True)
