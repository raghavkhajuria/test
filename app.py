import json

from flask import Flask, request, abort, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def index_new():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)
