import sqlite3
import os
from path_settings import *

# create DB
# check if empty
db_folder = os.path.join(CORE_FOLDER, 'db_folder')
if len(os.listdir(db_folder)) == 0:
    con = sqlite3.connect(os.path.join(db_folder, 'database.db'))
    cur = con.cursor()
    print('Database created successfully')
else:
    # if not, check for existing database
    for file in os.listdir(db_folder):
        if file.endswith('.db'):
            print('Database already exists')
            break
        else:
            con = sqlite3.connect(os.path.join(db_folder, 'database.db'))
            cur = con.cursor()
            print('Database created successfully')
