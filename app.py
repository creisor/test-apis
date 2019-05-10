import os
import time
import random
from flask import Flask, jsonify, request

class RandomError(Exception):
    status_code = 500

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

app = Flask(__name__)

@app.route('/')
def root():
    return jsonify(message="hello")

@app.route('/sleep')
def sleep():
    sleep_time = request.host.split(':')[-1][-1]
    if str(random.randint(1,5)) == sleep_time:
    #if str(1) == sleep_time:
        raise RandomError('Your (un)lucky day', status_code=506)
    time.sleep(int(sleep_time))
    return jsonify(appname="app{}".format(sleep_time),
                   sleeptime=sleep_time)

@app.errorhandler(RandomError)
def handle_random_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


