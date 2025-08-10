from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# Initialize your Slack app (NO socket_mode here)
app = App(token=os.getenv("BOT_TOKEN"))

# Langflow URL — Replace with your actual endpoint
LANGFLOW_URL = os.getenv("LANGFLOW_URL")
# Handle incoming messages
@app.message("")
def handle_message(message, say):
    user_input = message['text']
    user_id = message['user']  # Slack user ID for persistent session

    # Send to Langflow with session_id
    response = requests.post(LANGFLOW_URL, json={
        "output_type": "chat",
        "input_type": "chat",
        "input_value": user_input,
        "session_id": user_id
    })

    if response.status_code == 200:
        output = response.json()["outputs"][0]["outputs"][0]["results"]["message"]["text"]
        say(output)
    else:
        say("Oops! Error from Langflow.")

# Run the app with SocketModeHandler
if __name__ == "__main__":
    handler = SocketModeHandler(app, os.getenv("APP_TOKEN"))
    handler.start()

