import logging
import os
import sys
from datetime import datetime

from src.exception import CustomException

# Create a unique file name
LOG_FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create a directory path
DIR_PATH = os.path.join(os.getcwd(), "logs", LOG_FILE_NAME)
os.makedirs(DIR_PATH, exist_ok=True)

# Create file path
LOG_FILE_PATH = os.path.join(DIR_PATH, LOG_FILE_NAME)


# Create a log
logging.basicConfig(filename=LOG_FILE_PATH, format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s", level=logging.INFO)