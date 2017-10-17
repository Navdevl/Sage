from config import *
import datetime
import sqlite3
import string
import random


class Database:
  def __init__(self):
    """ 
    Initializing the database with local db file
    """
    self.conn = sqlite3.connect(SQLITE_DB)
    self.create()

  def name_generator(self, size=6, chars=string.ascii_uppercase + string.digits):
    """ 
    To create a random unique id for each reminder
    """
    return ''.join(random.choice(chars) for _ in range(size))

  def create(self):
    """ 
    Create the table if not exists
    See the documentation for the detailed information of table structure
    """
    self.conn.execute('''CREATE TABLE IF NOT EXISTS REMINDERS
             (UID VARCHAR2 PRIMARY KEY,
             SERVER_ID INTEGER NOT NULL,
             NAME TEXT NOT NULL DEFAULT test,
             FREQUENCY TEXT NOT NULL,
             REMIND_AT TEXT NOT NULL);''')

    self.conn.execute('''CREATE TABLE IF NOT EXISTS CHANNELS
             (SERVER_ID INTEGER NOT NULL,
             CHANNEL_ID INTEGER NOT NULL);''')

  def add_channel_to_server(self, server_id, channel_id):
    """ 
    Add default channel of the server
    """
    self.conn.execute("INSERT INTO CHANNELS (SERVER_ID, CHANNEL_ID) VALUES ('{0}', '{1}');".format(server_id, channel_id))
    return self.commit()

  def add_reminder(self, name, server_id, frequency, time):
    """ 
    Add Reminder to the database
    """
    uid = self.name_generator()
    self.conn.execute("INSERT INTO REMINDERS (UID, NAME, SERVER_ID, FREQUENCY, REMIND_AT) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}');".format(uid, name, server_id, frequency, time))
      return self.commit()

  def fetch_reminders(self, remind_time = datetime.datetime.now().strftime("%H:%M:00")):
    return self.conn.execute("SELECT * FROM REMINDERS where REMIND_AT = '{0}';".format(remind_time, server_id)).fetchall()

  def delete_reminder(self, uid, server_id):
    self.conn.execute("DELETE FROM REMINDERS WHERE UID = '{0}' AND SERVER_ID = '{1}';".format(uid, server_id))
    return self.commit()

  def show_all(self, server_id):    
    results = self.conn.execute("SELECT * from REMINDERS WHERE SERVER_ID = {0};".format(server_id)).fetchall()
    return results

  def commit(self):
    try:
      self.conn.commit()
      return True
    except:
      return False

  def close(self):
    self.conn.close()

