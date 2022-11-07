from path_settings import *


# initialize inputs
while True:
    try:

        user_input = int(input(
            f'''
        ==========================
        0. Exit

        1. Create Database
        2. Get Info
        ==========================
        '''))

        if user_input == 0:
            break

        elif user_input == 1:
            exec(open(os.path.join(CORE_FOLDER, 'create_db.py')).read())
        elif user_input == 2:
            exec(open(os.path.join(CORE_FOLDER, 'get_info.py')).read())
    except ValueError:
        print('Wrong input value')
