from distutils.command.config import config
from sharing.config.configuration import *
import logging

def main():
    try:
        config = Configuartion().get_training_pipeline_config()
        print(config)
    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__ == "__main__":
    main()