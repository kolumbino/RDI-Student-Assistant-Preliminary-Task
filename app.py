from flask import Flask, request, render_template
import requests
import os
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)


API_KEY = os.getenv("NEWS_API_KEY")
BASE_URL = "https://newsapi.org/v2/top-headlines"


@app.route('/')
def index():
    country = 'us'
    response = requests.get(f"{BASE_URL}?country={country}&apiKey={API_KEY}")
    articles = response.json().get('articles', [])
    return render_template('index.html', articles=articles)


@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.form.get('query')
    response = requests.get(f"{BASE_URL}?q={query}&apiKey={API_KEY}")
    articles = response.json().get('articles', [])
    return render_template('search.html', articles=articles)


if __name__ == '__main__':
    app.run(debug=True)
