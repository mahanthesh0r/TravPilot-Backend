"""

# THIS CODE DOES NOT WORK 

"""


from telethon import TelegramClient, events
import asyncio
from typing import Union

from fastapi import FastAPI

api_id = '27979168'
api_hash = 'ecddf025db1ae087e5ede2fe5d376760'
bot_username = '@duplicatetestbot'

client = TelegramClient('anon', api_id, api_hash)

async def main():
    await client.start()
    await client.send_message(bot_username, '@duplicatetestbot, Allocated_Budget: 4000, Initiation_Time: April 8, 2024 23:59 Return_Time: April 25, 2024 23:59, Kickoff_Spot: San Fransisco, Intended_Destination: New York ')

# Wait for a while to let the bot respond
    await asyncio.sleep(10)

    # Get the last 100 messages from the bot
    messages = await client.get_messages(bot_username, limit=1)
    for message in messages:
        print(message.text)

    await client.run_until_disconnected()

# Run the main function
loop = asyncio.get_event_loop()
loop.run_until_complete(main())