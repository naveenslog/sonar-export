import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
URL = os.environ.get("URL")
PROJECT = os.environ.get("PROJECT")