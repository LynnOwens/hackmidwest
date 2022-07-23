import argparse

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return "foo"


@app.route("/activate", methods=['POST'])
def process_term():
    print(request.get_json())
    return 'foozbaz'


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PI Daemon")
    parser.add_argument('listenIp', help='The listen IP of the site')
    parser.add_argument('listenPort', help='The listen port of the site')
    args = parser.parse_args()
    app.run(host=args.listenIp, port=args.listenPort, debug=True)
