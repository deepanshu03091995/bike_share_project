import sys,pip,os,json

from flask import Flask,send_file, abort, render_template
from sharing.logger import logging
from sharing.exception import SharingException
from sharing.config.configuration import Configuartion
from sharing.constant import CONFIG_DIR, get_current_time_stamp
from sharing.pipeline.pipeline import Pipeline


app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        sharing = SharingException(e,sys)
        logging.info(sharing.error_message)
    logging.info("Testing logger module")
    return "CI CD pipeline established."


if __name__=="__main__":
    app.run(debug=True)