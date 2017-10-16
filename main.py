import discord 
import asyncio
import re 
import datetime
from database import Database
from config import *
from messages import *

class Main:
  def __init__(self):
    self.client = discord.Client()
    self.client.loop.create_task(self.remind())
    self.db = Database()
    self.channel = None

  def convert_to_message(self, results):
    message = '```'
    if results is not None:
      for result in results:
        message += "{0} - Reminder to {1} at {2} \n".format(result[0], result[1].strip(), result[3])
    return message + '```'

  def extract_components(self, message):
    pattern = "\S+\sto\s(.+)at\s([0-9]+\:[0-9]+[am|pm]*)"
    match = re.match(pattern, message)
    if match is not None:
      return match.groups()
    return None

  def extract_uid(self, message):
    pattern = "!delete (.+)"
    match = re.match(pattern, message)
    if match is not None:
      return match.groups()[0]
    return None

  async def remind(self):
    await self.client.wait_until_ready()
    if self.channel is None:
      await asyncio.sleep(60)
    while not self.client.is_closed:
      now = datetime.datetime.now().strftime("%H:%M:00")
      print(now)
      results = self.db.fetch_reminders(now)
      print(results)
      for result in results:
        task = result[1]
        message_to_send = "Reminding @everyone to {0}".format(task)
        await self.client.send_message(self.channel, message_to_send)
      await asyncio.sleep(60) # task runs every 60 seconds

  def check_channel_initialized(self):
    if self.channel is None:
      # await self.client.send_message(self.channel, 'Initialize the channel')
      return False

  def run(self):
    @self.client.event
    async def on_ready():
      print('Logged in as:')
      print(self.client.user.name)

    @self.client.event
    async def on_message(message):
      if message.content == '!init':
        self.channel = message.channel
        await self.client.send_message(self.channel, "{0} is initialized for showing reminders".format(message.channel.name))

      if self.check_channel_initialized() is False:
        await self.client.send_message(self.channel, 'Initialize the channel')
        return

      if '!list' in message.content:
        results = self.db.show_all()
        message_to_send = self.convert_to_message(results)
        if message_to_send is '':
          message_to_send = 'No reminders'
        await self.client.send_message(self.channel, message_to_send)

      elif message.content == '!help':
        message_to_send = REMIND_HELP
        await self.client.send_message(self.channel, message_to_send)

      elif '!delete' in message.content:
        uid = self.extract_uid(message.content)
        if uid is not None:
          self.db.delete_reminder(uid)
        await self.client.send_message(self.channel, 'Deleted Successfully')

      elif '!remind' in message.content:
        result = self.extract_components(message.content)
        if result is not None:
          try:
            time = datetime.datetime.strptime(result[1], '%I:%M%p').time()
          except:
            time = datetime.datetime.strptime(result[1], '%I:%M').time()
          name = result[0]
          if self.db.add_reminder(name, 'daily', time):
            await self.client.send_message(self.channel, "Added reminder to {0} at {1} :smile:".format(result[0], result[1]))
          else:
            await self.client.send_message(self.channel, 'Something went wrong.!')  

    self.client.run(TOKEN)

obj = Main()
obj.run()