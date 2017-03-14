import json
import os

from flask import Flask, request, abort, jsonify, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index_new():
    return render_template('test.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
