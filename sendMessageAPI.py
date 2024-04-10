from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from telethon import TelegramClient, events
import asyncio
import json
from fastapi.responses import JSONResponse
import codecs


api_id = '29838225'
api_hash = '86382a33f53efbf3e51b3e4fa7bf1880'
bot_username = '@TravPilotFinalBot'

client = TelegramClient('anon', api_id, api_hash)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3000/itenary", "*"],
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/sendMessage")
async def send_message(budget:str,from_city:str,to_city:str,start_date:str,end_date:str):
    await client.start()
    #await client.send_message(bot_username, "@TravPilotFinalBot, totalBudget: "+ budget + " outboundLocation:"+ from_city + " returnLocation: " + to_city + " startDate: 04-20-2024" + " endDate: 04-22-2024")
    await client.send_message(bot_username,'"@TravPilotFinalBot, "totalBudget": 500,"outboundLocation": "' + to_city + '","returnLocation": "' + from_city + '","startDate": "04-23-2024","endDate": "04-25-2024"')



@app.get("/getMessage")
async def get_message():
    await client.start()
    # Get the last message from the bot
    messages = await client.get_messages(bot_username, limit=1)
    data =  messages[0].text
   # data = data.replace('\\"', '"').replace('\n', '').replace('\\', '')  
    #data = data.replace('\\\\', '') 
    
    with open("output.json", "w", encoding="utf-8") as file:
        # Write the data string to the file
        file.write(data)

    # Open the text file in read mode
    with open("output.json", "r") as file:
        # Read the data from the file
        newdata = file.read()
        newdata = newdata.replace(u"\u00A0", " ")

    outer_layer = json.loads(newdata)
    inner_json = json.loads(outer_layer["data"]) 

    return inner_json

@app.get("/testMessage")
async def sendTest():
    raw_data = r"""
                    {
                    "data": "{\"flight\":{\"flightUrl\":\"https://www.google.com/travel/flights?hl=en&gl=us&q=Flights+to+LAX+from+SFO+on+2024-04-08+through+2024-04-10\",\"flightPrice\":128,\"flightArrivalTime\":\"2024-04-09 00:36\"},\"hotel\":{\"hotelAddress\":\"120 S Los Angeles St, Los Angeles, CA 90012, United States\",\"hotelName\":\"DoubleTree by Hilton Hotel Los Angeles Downtown\",\"hotelURL\":\"https://www.url.com\"},\"days\":[{\"breakfast\":{\"name\":\"Jin China Bistro\",\"address\":\"123 Astronaut Ellison S Onizuka St Suite #202, Los Angeles, CA 90012, United States\",\"URL\":\"https://www.yelp.com/biz/jin-china-bistro-los-angeles?osq=cheap+food\"},\"entertainment1\":{\"name\":\"\",\"address\":\"the address\",\"URL\":\"https://www.URL.com\"},\"lunch\":{\"name\":\"Dino’s Chicken and Burgers\",\"address\":\"2575 W Pico Blvd, Los Angeles, CA 90006, United States\",\"URL\":\"https://www.yelp.com/biz/dinos-chicken-and-burgers-los-angeles?osq=cheap+food\"},\"entertainment2\":{\"name\":\"City National Plaza Fountain\",\"address\":\"the address\",\"URL\":\"https://www.URL.com\"},\"dinner\":{\"name\":\"K’Grill Korean Cuisine\",\"address\":\"404 S Figueroa St, Los Angeles, CA 90071, United States\",\"URL\":\"https://www.yelp.com/biz/kgrill-korean-cuisine-los-angeles-2?osq=cheap+food\"},\"entertainment3\":{\"name\":\"Kyoto Garden\",\"address\":\"the address\",\"URL\":\"https://www.URL.com\"}},{\"breakfast\":{\"name\":\"BROKEN MOUTH | Lee’s Homestyle\",\"address\":\"718 S Los Angeles St, Los Angeles, CA 90014, United States\",\"URL\":\"https://www.yelp.com/biz/broken-mouth-lees-homestyle-los-angeles-5?osq=cheap+food\"},\"entertainment1\":{\"name\":\"Kyoto Garden\",\"address\":\"the address\",\"URL\":\"https://www.URL.com\"},\"lunch\":{\"name\":\"BROKEN MOUTH | Lee’s Homestyle\",\"address\":\"718 S Los Angeles St, Los Angeles, CA 90014, United States\",\"URL\":\"https://www.yelp.com/biz/broken-mouth-lees-homestyle-los-angeles-5?osq=cheap+food\"},\"entertainment2\":{\"name\":\"Arthur J. Will Memorial Fountain\",\"address\":\"the address\",\"URL\":\"https://www.URL.com\"},\"dinner\":{\"name\":\"Dollar Hits\",\"address\":\"2432 W Temple St, Los Angeles, CA 90026, United States\",\"URL\":\"https://www.yelp.com/biz/dollar-hits-los-angeles-2?osq=cheap+food\"},\"entertainment3\":{\"name\":\"Griffith Park\",\"address\":\"the address\",\"URL\":\"https://www.URL.com\"}}]}",
                    "totalDays": 0
                    }

                    """

    outer_layer = json.loads(raw_data)
    inner_json = json.loads(outer_layer['data'])

    return inner_json