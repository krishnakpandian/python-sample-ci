"""
This file should request and create a Slack Post
"""

from config.config import get_slack_endpoint_url
import requests


"""
@description: This is description 1
@params: None
@return:
"""
# def authenticate_slack():
#     app = App(
#         token=os.environ.get("SLACK_BOT_TOKEN"),
#         signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
#     )
#     return app

''' @description: This is description 2 @params: None @return: '''
def create_slack_post(message:str = ''):
    payload = '{"text": "%s"}' % message
    res = requests.post(get_slack_endpoint_url(), data = payload)
    return res.text
