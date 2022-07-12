import sys
from flask import Flask
from sharing.logger import logging
from sharing.exception import SharingException
app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("Testing Exception  module")
    except Exception as e:
        sharing = SharingException(e,sys)
        logging.info(sharing.error_message)
    logging.info("Testing logger module")
    return "CI CD pipeline has been established."


if __name__=="__main__":
    app.run(debug=True)