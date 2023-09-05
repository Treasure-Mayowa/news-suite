from flask import Flask, render_template
from newsapi import NewsApiClient
import requests

app = Flask("News App")

newsapi = NewsApiClient(api_key="c9f2d1243a7a4d9db6747308edb117ce")

API_KEY = "c9f2d1243a7a4d9db6747308edb117ce"

@app.route("/")
def news():
    news = newsapi.get_top_headlines(language="en")
    return render_template("index.html", news=news["articles"])


@app.route("/news/<country_code>")
def news_country(country_code):
    top_headlines = requests.get(f"https://newsapi.org/v2/top-headlines?country={country_code}&apiKey=c9f2d1243a7a4d9db6747308edb117ce").json()
    return render_template("news_country.html", news=top_headlines["articles"])
