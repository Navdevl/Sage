import re
import datetime

class Extractor:
  def __init__(self):
    pass

  def extract_reminder_components(self, message):
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

  def extract_time(self, time):
    try:
      converted_time = datetime.datetime.strptime(time, '%I:%M%p').time()
    except:
      converted_time = datetime.datetime.strptime(time, '%I:%M').time()
    return converted_time