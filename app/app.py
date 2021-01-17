from flask import Flask, request, redirect, render_template

from .config import URL, CLIENT_ID
from .utils import get_photo_url


app = Flask(__name__)


@app.route('/')
def home():
    query = request.args.get('query', '')
    if query:
        return redirect(get_photo_url(URL, CLIENT_ID, query))
    else:
        return render_template('index.html')
