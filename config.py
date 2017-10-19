import os

CURR_DIR = os.getcwd()
DATABASE_DIR = os.path.join(CURR_DIR, 'database')

TOKEN = 'MzcwNDkxNjU4NzY2MjU0MDky.DMn22A.2ayZZlte12AcCSWt2XYeDG-yicM'
SQLITE_DB = os.path.join(DATABASE_DIR, 'test.db')

REMIND_HELP = '```!remind to {message} at {HH:MMam|pm} \n\nExample:\n\t !remind to order tea at 11:00am```'