import base64
import configparser
import json
import os
import pdfkit
import sys

import logging

# create logger
logger = logging.getLogger('print_handler_cli')
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


args = None
if len(sys.argv) > 0:
    args = json.loads(sys.argv[1].replace("\'", "\""))

if args:
    try:
        url = args["url"] if "url" in args else None
        content = args["content"] if "content" in args else None
        options = args["options"]
        printer_name = args["printer_name"]

    except Exception as e:
        logger.error(e)

config = configparser.ConfigParser()
config.read('app.ini')
WKHTMLTOPDF_PATH = config["default"]["WKHTMLTOPDF_PATH"]

config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)

if content:
    logger.info("content " + content)
    decoded_content = base64.b64decode(content).decode("utf-8")
    logger.info("decoded content " + decoded_content)
    rs = pdfkit.from_string(
        decoded_content,
        "out.pdf",
        configuration=config,
        options=options
    )

if url:
    logger.info("url {}" + url)
    rs = pdfkit.from_url(
        url,
        "out.pdf",
        configuration=config,
        options=options
    )

logger.info("print to out.pdf")
os.system("RUNDLL32 PRINTUI.DLL,PrintUIEntry /y /n \"{}\"".format(printer_name))
os.startfile("out.pdf", "print")
