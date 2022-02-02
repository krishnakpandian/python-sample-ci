import os
from dotenv import load_dotenv

load_dotenv()

def get_slack_endpoint_url() -> str:
    return os.getenv('SLACK_BOT_ENDPOINT')