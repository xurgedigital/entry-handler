from ast import alias
from multiprocessing.connection import wait
import discord
from discord.utils import get
from discord.ext import commands
import logging
from pathlib import Path
import platform
import json
import os
from discord import Guild
import asyncio
from requests_html import HTMLSession 
from requests_html import AsyncHTMLSession
from bs4 import BeautifulSoup as bs # importing BeautifulSoup

cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n-----")
bot = commands.Bot(command_prefix='!!',
                   description='Verifier Bot',
                   case_insensitive=True,
                   #ownder_id=739375301578194944,
                   owner_id=600498789362565123,
                   help_command=None)
bot.config_token = (
    #"OTc1Nzc4ODQwMzE4MTg1NTUy.GO2sP9.bhOhCI-Ar2-_yf_yd1XTzRAQjc98-R9ZJYKggc")
    "OTUyNjUzMjQ1MDI3ODYwNTcw.G4Icab.SBF8-YdltFUCf-dYinIt_dfWhbxsFY-4xskQ8Y")
logging.basicConfig(level=logging.INFO)

# def get_data(url):
#     session = HTMLSession()
#     response = session.get(url)
#     response.html.render(sleep=1)
#     soup = bs(response.html.html, "html.parser")
#     youtube_time=soup.find("meta", itemprop="datePublished")["content"]
#     youtube_description=soup.find("meta", itemprop="description")["content"]
#     return youtube_time, youtube_description

bot.counter=0
#if (message.channel.id == 997762353284259920): 
@bot.event
async def on_message(message):
  if (message.channel.id == 997762353284259920) & ('https://twitter.com/' in message.content):
    emoji='🤖'
    #emoji='✅'
  # for i in embeds:
  #   a=i.to_dict()
  #   name=a['author']['name']
    
        
  # bot.counter += 1
    if message.author == bot.user:
      return
    if 'https://twitter.com/' in message.content:
      try:
          await asyncio.sleep(1.2)
          embeds = message.embeds
          for embed in embeds:
            usrdata = embed.to_dict()
            data = {
              "url":message.content,
              "discord_time":str(message.created_at),
              "usr_discord":message.author.id,
              "body":usrdata['description'],
              "message_id":message.id,
              "SM_username":usrdata['author']['name'],
              "twitter_timestamp":usrdata['timestamp'],
            }
            print("Received from discord: ", data)
            # await message.channel.send(data)
            with open('users.json', 'r+') as f:
              json_object = json.load(f)
              # await message.channel.send(json_object)
              list1 = json_object['entries']
              # list1.clear()
              list1.append(data)
              json_object["entries"] = list1
              f.seek(0)
              json.dump(json_object, f, indent=4)
              f.truncate()
            # headers={"Bearer":"5a3816a4942b83949579741785e73b38"}
            # r = requests.post("https://xurge-coming.bubbleapps.io/version-test/api/1.1/wf/entries/?start_id=11111111&end_id=22222222",headers=headers,json=json_object)
            # await message.channel.send(f'User:{user.mention}\nStatus code:{r.status_code}\nReason:{r.reason}')
            # await message.channel.send(f'{user.mention}\nRecorded')
            await message.add_reaction(emoji)
      except Exception as e:
        await message.channel.send(f'Error message: {e}')
    if 'https://www.youtube.com/' in message.content or 'https://youtu.be/' in message.content:
      try:
        await asyncio.sleep(1.2)
        embeds2 = message.embeds
        for embed in embeds2:
            usrdata1 = embed.to_dict()
            data = {
              "url":message.content,
              "discord_time":str(message.created_at),
              "usr_discord":message.author.id,
              "message_id":message.id,
              "body":"",
              "SM_username":usrdata1['author']['name'],
              "youtube_time":""
            }
            print("Received from discord: ", data)
            with open('users.json', 'r+') as f:
              json_object = json.load(f)
              # await message.channel.send(json_object)
              list1 = json_object['entries']
              # list1.clear()
              list1.append(data)
              json_object["entries"] = list1
              f.seek(0)
              json.dump(json_object, f, indent=4)
              f.truncate()
            await message.add_reaction(emoji)
      except Exception as e:
        await message.channel.send(f'Error message: {e}')
bot.run(bot.config_token)  # Runs our bot
