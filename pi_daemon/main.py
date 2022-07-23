import argparse
import asyncio

from flask import Flask, request
from kasa import Discover
from kasa.discover import DeviceDict

app = Flask(__name__)


@app.route("/")
def index():
    return "foo"


@app.route("/activate", methods=['POST'])
def process_term():
    print(request.get_json())
    devices: DeviceDict = discover_devices()
    for addr, dev in devices.items():
        asyncio.run(dev.update())
        print(f"{addr} >> {dev}")
    return 'foozbaz'


def discover_devices() -> DeviceDict:
    return asyncio.run(Discover.discover())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PI Daemon")
    parser.add_argument('listenIp', help='The listen IP of the site')
    parser.add_argument('listenPort', help='The listen port of the site')
    args = parser.parse_args()
    app.run(host=args.listenIp, port=args.listenPort, debug=True)
