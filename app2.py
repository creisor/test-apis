import time
from flask import Flask, jsonify
app = Flask(__name__)

SLEEP_TIME = 10

@app.route('/')
def root():
	time.sleep(SLEEP_TIME)
	return jsonify(appname="app2",
			       sleeptime=SLEEP_TIME)
