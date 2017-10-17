from extractor import Extractor
from database import Database
import asyncio
import discord

class Message:
  def __init__(self):
    self.db = Database()
    self.extractor = Extractor()

  def message_for_list(self, server_id):
    results = self.db.show_all(server_id)
    message_to_send = self.convert_to_message(results)
    if message_to_send is '':
      message_to_send = 'No reminders'
    return message_to_send

  def message_for_remind(self, message):
    result = self.extractor.extract_reminder_components(message.content)
    if result is not None:
      time = self.extractor.extract_time(result[1])
      name = result[0].strip()
      if self.db.add_reminder(name, message.server.id, 'daily', time):
        return "Added reminder to {0} at {1} :smile:".format(result[0], result[1])
      else:
        return 'Oops. Something went wrong.!'

  def message_for_delete(self, message):
    uid = self.extractor.extract_uid(message.content)
    if uid is not None:
      if self.db.delete_reminder(uid, message.server.id):
        return 'Deleted Successfully'
      else:
        return 'Sorry, No such UID'
    else:
        return 'Oops. Something went wrong.!'

  def message_for_help(self):
    return REMIND_HELP
    

  def convert_to_message(self, results):
    message = '```'
    if len(results) > 0:
      for result in results:
        message += "{0} - Reminder to {1} at {2} \n".format(result[0], result[2], result[4])
    else:
      return ''
    return message + '```'