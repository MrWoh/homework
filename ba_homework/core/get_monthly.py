import shutil
import datetime as dt
from calendar import monthrange
import pandas as pd
import os.path
from path_settings import UNC_FILE_FOLDER, C_FILE_FOLDER

unc_data = os.path.join(UNC_FILE_FOLDER, '')

# find all days data
for file in os.listdir(unc_data):
    df = pd.read_parquet(os.path.join(unc_data, file))
    date = df.loc[0:0, 'tpep_pickup_datetime'].values.astype(str)
    date = date[0].split('-')
    year, month = int(date[0]), int(date[1])
    if file.endswith('.parquet'):
        if file.endswith('.parquet'):
            num_days = monthrange(year, month)
            for day in range(2, num_days[1]+1):
                df = df[df.tpep_dropoff_datetime.dt.date ==
                        dt.date(int(year), int(month), day)]
                file_name = os.path.join(
                    unc_data, 'yellow_tripdata_{}-{}-{}.parquet'.format(int(year), int(month), day))
                df.to_parquet(file_name, engine='fastparquet')
    c_data_new_folder = 'yellow_tripdata_{}-{}'.format(int(year), int(month))
    c_data_move_dest = os.path.join(C_FILE_FOLDER, c_data_new_folder, '')
    os.mkdir(c_data_move_dest)
    # fetch all files
    for file_name in os.listdir(unc_data):
        # construct full file path
        source = unc_data + file_name
        destination = c_data_move_dest + file_name
        # move only files
        if os.path.isfile(source):
            shutil.move(source, destination)
