import os
import time
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def root():
    return jsonify(message="hello")

@app.route('/sleep')
def sleep():
    sleep_time = request.host.split(':')[-1][-1]
    time.sleep(int(sleep_time))
    return jsonify(appname="app{}".format(sleep_time),
                   sleeptime=sleep_time)
