import logging
import os
from datetime import datetime

# Creaye log directory 

LOG_DIR = "pylogs"
LOG_DIR_PATH = os.path.join(os.getcwd(),LOG_DIR)

os.makedirs(LOG_DIR,exist_ok=True)

# Create logfile name 

CURRENT_TIME_STAMP = f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}"

file_name = f"log_{CURRENT_TIME_STAMP}"
log_file_path = os.path.join(LOG_DIR,file_name)

# Configure logging 
logging.basicConfig(level=logging.INFO,
                    filename=log_file_path,
                    format="%(asctime)s %(levelname)s %(module)s =============> %(message)s",
                    datefmt= "%d-%m-%y %H:%M"
                  )



logger = logging.getLogger()
