#!/usr/bin/python3
# Starts a Flask web app
from flask import Flask
if __name__ == "__main__":
	app = Flask(__name__)

	@app.route('/')
	
