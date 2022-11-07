import os

MAIN_FOLDER = os.path.dirname(__file__)
CORE_FOLDER = os.path.join(MAIN_FOLDER, 'core')
DB_FOLDER = os.path.join(CORE_FOLDER, 'database')
CREATE_DB = os.path.join(CORE_FOLDER, 'create_db.py')
UNC_FILE_FOLDER = os.path.join(MAIN_FOLDER, 'file_uncompiled')
C_FILE_FOLDER = os.path.join(MAIN_FOLDER, 'file_compiled')
