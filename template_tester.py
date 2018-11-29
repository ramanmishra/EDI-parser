from flask import Flask
import json

app = Flask(__name__)


@app.route('/test/test_josn/<jsonString>', methods=['POST'])
def test_json(jsonString):
    try:
        json.loads(jsonString)
        return True
    except Exception as ex:
        return ex

app.run()

