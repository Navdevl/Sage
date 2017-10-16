from config import *
import datetime
import sqlite3
import string
import random


class Database:
  def __init__(self):
    self.conn = sqlite3.connect(SQLITE_DB)
    self.create()

  def name_generator(self, size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

  def create(self):
    self.conn.execute('''CREATE TABLE IF NOT EXISTS REMINDERS
             (UID VARCHAR2 PRIMARY KEY,
             NAME TEXT NOT NULL DEFAULT test,
             FREQUENCY TEXT NOT NULL,
             REMIND_AT TEXT NOT NULL);''')

  def close(self):
    self.conn.close()

  def fetch_reminders(self, remind_time):
    return self.conn.execute("SELECT * FROM REMINDERS where REMIND_AT = '{0}';".format(remind_time)).fetchall()


  def add_reminder(self, name, frequency, time):
    uid = self.name_generator()
    self.conn.execute("INSERT INTO REMINDERS (UID, NAME, FREQUENCY, REMIND_AT) VALUES ('{0}', '{1}', '{2}', '{3}');".format(uid, name, frequency, time))
    try:
      self.conn.commit()
      return True
    except:
      return False

  def delete_reminder(self, uid):
    self.conn.execute("DELETE FROM REMINDERS WHERE UID = '{0}';".format(uid))
    self.conn.commit()

  def add_test_reminder(self):
    remind_at = datetime.datetime.now()
    self.conn.execute("INSERT INTO REMINDERS (NAME, FREQUENCY, REMIND_AT) VALUES ('test', 'daily', '2017-10-13 16:16:00.071742');")
    self.conn.commit()

  def show_all(self):    
    results = self.conn.execute("SELECT * from REMINDERS;").fetchall()
    return results


