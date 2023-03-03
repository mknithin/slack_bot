import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_sdk.models.blocks import *

client = WebClient(token="bot_token")

blocks = [
    SectionBlock(
        text="Hello! This is a message with a button.",
        accessory=ButtonElement(
            text="block",
            action_id="block_user",
            value="h324234234234234"
        )
    )
]


try:
    response = client.chat_postMessage(
        channel="#random",
        blocks=blocks
    )
    print("Message sent: ", response["ts"])
except SlackApiError as e:
    print("Error sending message: ", e)