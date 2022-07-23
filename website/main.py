from flask import Flask
import argparse

app = Flask(__name__)


@app.route("/")
def index():
    return "Congratulations, it's a web app!"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SBS GitLab Project Management Tool")
    parser.add_argument('listenIp', help='The listen IP of the site')
    parser.add_argument('listenPort', help='The listen port of the site')
    args = parser.parse_args()
    app.run(host=args.listenIp, port=args.listenPort, debug=True)
