import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

url_endpoint_from_env = os.environ.get("URL_ENDPOINT")
login_id = os.environ.get("LOGIN_ID")
login_pw = os.environ.get("LOGIN_PW")
notify_token = os.environ.get("NOTIFY_TOKEN")


URL_ENDPOINT: str = url_endpoint_from_env if url_endpoint_from_env is not None else ""
LOGIN_ID: str = login_id if login_id is not None else ""
LOGIN_PW: str = login_pw if login_pw is not None else ""
NOTIFY_TOKEN = notify_token if notify_token is not None else ""
