import os

from dotenv import load_dotenv
from tamga import Tamga

load_dotenv()
DEV = os.getenv("DEV")

logger = Tamga(
    isColored=DEV,
    logToJSON=DEV,
)


print(DEV)
