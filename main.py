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

  async def remind(self):
    await self.client.wait_until_ready()
    while not self.client.is_closed:
      now = datetime.datetime.now().strftime("%H:%M:00")
      results = self.db.fetch_reminders(now)
      for result in results:
        task = result[2]
        message_to_send = "Reminding @everyone to {0}".format(task)
        channel = self.client.get_channel(str(result[6]))
        await self.client.send_message(channel, message_to_send)
      await asyncio.sleep(60) # task runs every 60 seconds

  def get_server_channel(self, server):
    channel_info = self.db.get_server_channel(server.id)
    if len(channel_info) > 0:
      channel = self.client.get_channel(str(channel_info[0][1]))
      return channel
    return None

  def run(self):
    @self.client.event
    async def on_ready():
      print('Logged in as:')
      print(self.client.user.name)

    @self.client.event
    async def on_message(message):
      if message.author == self.client.user:
        return

      message.content = message.content.lower()
      channel = self.get_server_channel(message.server)

      if message.content == '!init':
        message_to_send = self.message.message_for_init(message)
        await self.client.send_message(message.channel, message_to_send)
        return

      if channel is None:
        return await self.client.send_message(message.channel, 'Initialize a channel using `!init`')

      if '!list' in message.content:
        message_to_send = self.message.message_for_list(message.server.id)
        await self.client.send_message(channel, message_to_send)

      elif message.content == '!help':
        message_to_send = self.message.message_for_help()
        await self.client.send_message(channel, message_to_send)

      elif '!delete' in message.content:
        message_to_send = self.message.message_for_delete(message)
        await self.client.send_message(channel, message_to_send)

      elif '!remind' in message.content:
        message_to_send = self.message.message_for_remind(message)
        await self.client.send_message(channel, message_to_send)

    self.client.run(TOKEN)

obj = Main()
obj.run()