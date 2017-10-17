import os

CURR_DIR = os.getcwd()
DATABASE_DIR = os.path.join(CURR_DIR, 'database')

TOKEN = 'MzY2MDkwNzEyMDg2ODcyMDY0.DMFUiQ.j8QUdEQWfJBh8U5QFlcELztcMCA'
SQLITE_DB = os.path.join(DATABASE_DIR, 'test.db')

REMIND_HELP = '```!remind to {message} at {HH:MMam|pm} \n\nExample:\n\t !remind to order tea at 11:00am```'