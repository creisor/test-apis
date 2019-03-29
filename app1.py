import time
from flask import Flask, jsonify
app = Flask(__name__)

SLEEP_TIME = 5

@app.route('/')
def root():
	time.sleep(SLEEP_TIME)
	return jsonify(appname="app1",
			       sleeptime=SLEEP_TIME)
