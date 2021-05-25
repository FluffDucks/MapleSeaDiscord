import os
import discord
from discord.ext import commands
from termcolor import colored
import requests
import json
from dotenv import load_dotenv
from d2t_formatter import format_content

# Declare disc vars
load_dotenv()
D_TOKEN = os.getenv('D_TOKEN')
DCHANNEL_ID = os.getenv('DCHANNEL_ID')
POST_URL = os.getenv('POST_URL')

client = commands.Bot(command_prefix='')

@client.event
async def on_ready():
  print(colored('SYS: dbot {0.user} is now live!'.format(client), 'blue'))

@client.event
async def on_message(message):
  print(colored('DISC: message received', 'blue'))
  # check that message is from our maplesea-announcements channel
  if str(message.channel.id) == DCHANNEL_ID:
    # Logging
    print(colored('DISC: Message from maplesea-announcements channel received:\n\t{}'.format(message.content), 'blue'))
    # Build message object
    formatted_content = format_content(message.content)
    print('FORMATTED - ' + formatted_content)
    msg = { 
      'title': '',
      'body': formatted_content
    }
    # Forward to tele api
    r = requests.post(POST_URL, data=json.dumps(msg))
    print(colored('DISC: Posted to tele: {}'.format(r.text), 'blue'))
  else:
    print(colored('DISC: Message was not posted (incorrect channel id)', 'blue'))
  
client.run(D_TOKEN)

# TODO: Message edited?
# message object: <Message 
    #   id=844584112626335795 
    #   channel=<TextChannel 
    #             id=844288549507170314 
    #             name='maplesea-announcements' 
    #             position=0 
    #             nsfw=False 
    #             news=False 
    #             category_id=844286929100341290> 
    #   type=<MessageType.default: 0> 
    #   author=<Member id=392691520358055947 name='FluffDucks' discriminator='8030' bot=False nick=None guild=<Guild id=844286929100341289 name="FluffDucks' Dev Server" shard_id=None chunked=False member_count=2>> 
    #   flags=<MessageFlags value=0>>
    # if message.content.startswith('$hello'):
    #     await message.channel.send('Hello!')