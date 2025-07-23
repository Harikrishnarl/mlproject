import logging
import os
from datetime import datetime
logfile=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logpath=os.path.join(os.getcwd(),"logs",logfile)
os.makedirs(logpath,exist_ok=True)
logfielpath=os.path.join(logpath,logfile)
logging.basicConfig(
    filename=logfielpath,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)


        