import json

from flask import Flask, request

app = Flask(__name__)


@app.route('/test/', methods=['POST'])
def test():
    data = request.data

    try:
        json.loads(data)
        return "JsonString validated successfully"
    except Exception as e:
        return "Error Encountered: {}".format(e)


app.run()
