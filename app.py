from flask import Flask, url_for
from flask import render_template
from markupsafe import escape


app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/contact/')
def contact_():
    return render_template('contact.html')

@app.route('/catalog/')
def contact():
    return render_template('catalog.html')

if __name__ == '__main__':
    app.run()
