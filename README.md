# Slack Bot with Langflow Integration

A Slack bot that integrates with Langflow to provide AI-powered conversational responses. The bot receives messages from Slack users and forwards them to a Langflow API endpoint, then returns the AI-generated responses back to the Slack channel.

## Features

- Real-time message handling in Slack
- Integration with Langflow AI workflows
- Session-based conversations using Slack user IDs
- Environment variable configuration for security

## Prerequisites

- Python 3.10
- A Slack workspace and Slack App with Bot Token and App Token
- A running Langflow instance

## Setup Instructions

### 1. Clone and Navigate to Project

```bash
git clone <your-repo-url>
cd langflow-gifting-poc
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project root (or update the existing one) with your Slack tokens:

```env
BOT_TOKEN="xoxb-your-bot-token-here"
APP_TOKEN="xapp-your-app-token-here"
```

**How to get your tokens:**

#### Bot Token (BOT_TOKEN):
1. Go to [Slack API](https://api.slack.com/apps)
2. Select your app or create a new one
3. Go to "OAuth & Permissions" in the sidebar
4. Copy the "Bot User OAuth Token" (starts with `xoxb-`)

#### App Token (APP_TOKEN):
1. In your Slack app settings, go to "Basic Information"
2. Scroll down to "App-Level Tokens"
3. Create a new token with `connections:write` scope
4. Copy the token (starts with `xapp-`)

### 4. Configure Langflow URL

Update the `LANGFLOW_URL` in `slack.py` if needed:

```python
LANGFLOW_URL = "http://localhost:7860/api/v1/run/your-flow-id-here"
```

### 5. Slack App Configuration

Make sure your Slack app has the following:

#### Bot Token Scopes:
- `app_mentions:read`
- `channels:history`
- `chat:write`
- `im:history`
- `im:read`
- `im:write`

#### Event Subscriptions:
- Enable Events
- Subscribe to bot events: `message.channels`, `message.im`

#### Socket Mode:
- Enable Socket Mode in your app settings

## Running the Application

### Start Langflow (if running locally)
```bash
langflow run
```

### Start the Slack Bot
```bash
python slack.py
```

You should see output indicating the bot is starting and connecting to Slack.

## Usage

1. Invite your bot to a Slack channel or send it a direct message
2. Type any message to the bot
3. The bot will forward your message to Langflow and return the AI-generated response

## Project Structure

```
slack/
├── .env              # Environment variables (tokens)
├── requirements.txt  # Python dependencies
├── slack.py         # Main bot application
└── README.md        # This file
```