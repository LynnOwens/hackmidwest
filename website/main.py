import json
import subprocess

import requests
from flask import Flask, render_template, request
import argparse
from typing import List

from textblob import TextBlob

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('input_term.html')


@app.route("/process_term", methods=['POST'])
def process_term():
    return request.form['term']


def call_remote():
    response = requests.request('GET', 'https://www.google.com')
    print(response.content)


def average_list(data: List[float]) -> float:
    return sum(data) / len(data)


def analyze_sentiment(tweets: List[dict]):
    sentiments: List[float] = []
    for tweet in tweets:
        tweet_text_blob = TextBlob(tweet['text'])
        sentiments.append(tweet_text_blob.sentiment.polarity)
    print(str(average_list(sentiments)))


def read_data_file() -> List[dict]:
    with open('../twitter-client/tmp/data.json') as data_file:
        return json.load(data_file)['statuses']


def run_twitter_client():
    subprocess.run(['node', '../twitter-client/index.js'])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SBS GitLab Project Management Tool")
    parser.add_argument('listenIp', help='The listen IP of the site')
    parser.add_argument('listenPort', help='The listen port of the site')
    args = parser.parse_args()
    run_twitter_client()
    analyze_sentiment(read_data_file())
    app.run(host=args.listenIp, port=args.listenPort, debug=True)
