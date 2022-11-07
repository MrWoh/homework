import sqlite3
import os
from homework.path_settings import DB_FOLDER

# create DB
for file in os.listdir(DB_FOLDER):
    if file.endswith('.db'):
        print('Database already exists')
        break
    else:
        con = sqlite3.connect(os.path.join(
            DB_FOLDER, 'database.db'))
        cur = con.cursor()
        print('Database created successfully')
