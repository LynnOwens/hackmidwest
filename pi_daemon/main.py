import argparse
import asyncio
import subprocess

from flask import Flask, request
from kasa import Discover, SmartDevice, SmartPlug
from kasa.discover import DeviceDict

app = Flask(__name__)
devices: DeviceDict = None


@app.route("/")
def index():
    return "foo"


@app.route("/activate", methods=['POST'])
async def process_term():
    print(request.get_json())
    sentiment: float = request.get_json()['sentiment']
    # plug: SmartDevice = SmartPlug("192.168.2.8")
    # await plug.update()
    # await plug.turn_on()

    good_plug: SmartDevice = None
    bad_plug: SmartDevice = None
    for addr, dev in devices.items():
        if dev.alias.lower() == 'good':
            good_plug = dev
        elif dev.alias.lower() == 'bad':
            bad_plug = dev
        print(f"{addr} >> {dev}")

    if sentiment > 0:
        if good_plug:
            await good_plug.turn_on()
        if bad_plug:
            await bad_plug.turn_off()
    else:
        if good_plug:
            await good_plug.turn_off()
        if bad_plug:
            await bad_plug.turn_on()

    return 'foozbaz'


def discover_devices() -> DeviceDict:
    return asyncio.run(Discover.discover())


def turn_on(plug: SmartDevice):
    subprocess.run(['kasa', '--host', plug.host, 'on'], shell=True)


def turn_off(plug: SmartDevice):
    subprocess.run(['kasa', '--host', plug.host, 'off'], shell=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PI Daemon")
    parser.add_argument('listenIp', help='The listen IP of the site')
    parser.add_argument('listenPort', help='The listen port of the site')
    args = parser.parse_args()
    devices = discover_devices()
    app.run(host=args.listenIp, port=args.listenPort, debug=True)
