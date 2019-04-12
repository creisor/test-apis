import os
import time
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def root():
    return jsonify(message="hello")

@app.route('/sleep/<sleep_time>')
def sleep(sleep_time):
    time.sleep(int(sleep_time))
    return jsonify(appname="app1",
                   sleeptime=sleep_time)
