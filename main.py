import discord 
import asyncio
import re 
import datetime
from database import Database
from extractor import Extractor
from message import Message
from config import *

class Main:
  def __init__(self):
    self.client = discord.Client()
    self.client.loop.create_task(self.remind())
    self.db = Database()
    self.extractor = Extractor()
    self.message = Message()
    self.channel = None

  async def remind(self):
    await self.client.wait_until_ready()
    if self.channel is None:
      await asyncio.sleep(60)
    while not self.client.is_closed:
      now = datetime.datetime.now().strftime("%H:%M:00")
      results = self.db.fetch_reminders(now)
      for result in results:
        task = result[1]
        message_to_send = "Reminding @everyone to {0}".format(task)
        await self.client.send_message(self.channel, message_to_send)
      await asyncio.sleep(60) # task runs every 60 seconds

  def check_channel_initialized(self):
    if self.channel is None:
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
        await self.client.send_message(self.channel, "**{0}** is initialized for showing reminders".format(message.channel.name))

      if self.check_channel_initialized() is False:
        await self.client.send_message(self.channel, 'Initialize the channel using `!init`')
        return

      if '!list' in message.content:
        message_to_send = self.message.message_for_list()
        await self.client.send_message(self.channel, message_to_send)

      elif message.content == '!help':
        message_to_send = self.message.message_for_help()
        await self.client.send_message(self.channel, message_to_send)

      elif '!delete' in message.content:
        message_to_send = self.message.message_for_delete(message)
        await self.client.send_message(self.channel, message_to_send)

      elif '!remind' in message.content:
        message_to_send = self.message.message_for_remind(message)
        await self.client.send_message(self.channel, message_to_send)

    self.client.run(TOKEN)

obj = Main()
obj.run()