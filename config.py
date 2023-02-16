# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "25356202"))
API_HASH = os.environ.get("API_HASH", "d65d4aa3f001d165ce52acb7bcbe153f")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5867009362:AAGbG4Y40_I6dLQdwKMujsF7q_MAHocfrzU")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("5890495617")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://pawanjaatpk:pawanjaatpk@cluster0.espumjg.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "5402684050")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(5402684050)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001852972559")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "Shortusssite") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
