import os

from flask import Flask, request, json, abort, Response

import logging

# create logger
logger = logging.getLogger('print_handler_api')
logger.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)
logger.addHandler(ch)

fh = logging.FileHandler('app.log')
fh.setLevel(level=logging.INFO)
fh.setFormatter(formatter)
logger.addHandler(fh)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Printer Hub'


@app.route('/printer/print', methods=['POST', 'GET'])
def printer_print():
    if request.is_json:
        data = request.json
        logger.info(data)

        os.system('python print_handler.py "{}"'.format(data))

        return {"msg": "ok"}

    return Response("{'msg':'fail'}", status=400, mimetype='application/json', headers={'Access-Control-Allow-Origin':'*'})


if __name__ == '__main__':
    app.run()