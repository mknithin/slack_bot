from fastapi import FastAPI, Request, Body
from slack_bolt import App
from slack_bolt.adapter.fastapi import SlackRequestHandler
from slack_sdk.models.blocks import *
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_bolt.adapter.fastapi import SlackRequestHandler

app = FastAPI()

client = WebClient(token="bot_token") # can get from OAuth & Permissions

slack_app = App(
    token="bot_token",# can get from OAuth & Permissions
    signing_secret="Signing Secret" # can get from app Basic Information page
)

app_handler = SlackRequestHandler(slack_app)

# slack_app = App(token="xoxb-1370143350000-4915920125136-4S2T9vhaAFhQmpjzZOoExUAq")
# handler = SlackRequestHandler(slack_app)

@app.post("/slack/events")
async def slack_events_handler(request: Request):
    return await app_handler.handle(request)



# @app.post("/slack-block-user")
# async def slack_events_handler(request: Request, data= Body(...)):
#     event_data = await request.json()
#     if event_data.get("type") == "url_verification":
#         return event_data.get("challenge")
#     elif event_data.get("type") == "event_callback":
#         if event_data.get("event").get("type") == "block_user":
#             if event_data.get("event").get("text") == "block":
#                 blocks = [
#                     SectionBlock(
#                         text="Hello! This is a message with a button.",
#                         accessory=ButtonElement(
#                             text="block",
#                             action_id="block_user",
#                             value="h324234234234234"
#                         )
#                     )
#                 ]
#                 try:
#                     response = client.chat_postMessage(
#                         channel="#random",
#                         blocks=blocks
#                     )
#                     print("Message sent: ", response["ts"])
#                 except SlackApiError as e:
#                     print("Error sending message: ", e)
#     print(event_data)
#     return await handler.handle(request)

# @slack_app.action("block_user")
# async def handle_button_click(ack, body, logger):
#     logger.info(body)
#     # Do something here, like send a reply message
#     await ack("Button clicked!")
    
@slack_app.action("block_user")
def handle_some_action(ack, body, logger):
    ack()
    print(body)
    
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8044)