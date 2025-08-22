import logging 
import os
from logging.handlers import RotatingFileHandler
from datetime import datetime 
LOG_DIR=os.path.join(os.getcwd(),"logs")
os.makedirs(LOG_DIR,exist_ok=True)
LOG_FILE=os.path.join(LOG_DIR,"app.log")

LOG_FORMAT=(
    "%(asctime)s [%(levelname)s] %(name)s.%(funcName)s:%(lineno)d - %(message)s"
)
DATE_FORMAT="%Y-%m-%d %H:%M:%S"

formatter=logging.Formatter(LOG_FORMAT,datefmt=DATE_FORMAT)

file_handler=RotatingFileHandler(
    LOG_FILE,maxBytes=5*1024*1024, backupCount=5
)
file_handler.setFormatter(formatter)
logger=logging.getLogger("ml_pipeline")
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)
logger.propagate=False


if __name__=='__main__':
    logger.info("logging has started")



# logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
# os.makedirs(logs_path,exist_ok=True)

# LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

# logging.basicConfig(
#     filename=LOG_FILE_PATH,
#     format="%(asctime)s [%(levelname)s] %(name)s.%(funcName)s:%(lineno)d - %(message)s",
#     level=logging.INFO
# )
