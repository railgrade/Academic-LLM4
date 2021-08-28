import asyncio
from os import getenv

from dotenv import load_dotenv
from slack_sdk.web.async_client import AsyncWebClient
from slack_sdk.errors import SlackApiError

load_dotenv()
CLAUDE_BOT_ID = getenv("CLAUDE_BOT_ID")


class SlackClient(AsyncWebClient):

    CHANNEL_ID = None
    LAST_TS = None

    async def chat(self, text):
        if not self.CHANNEL_ID:
            raise Exception("Channel not found.")

        resp = await self.chat_postMessage(channel=self.CHANNEL_ID, text=text)
        print("c: ", resp)
        self.LAST_TS = resp["ts"]

    async def open_channel(self):
        if not self.CHANNEL_ID:
            response = await self.conversations_open(users=CLAUDE_BOT_ID)
            self.CHANNEL_ID = response["channel"]["id"]

    async def get_reply(self):
        for _ in range(150):
            try:
                resp = await self.conversations_history(channel=self.CHANNEL_ID, oldest=self.LAST_TS, limit=2)
                print("r: ", resp)
                msg = [msg["text"] for msg in res