import datetime as dt
from calendar import monthrange
import pandas as pd
import os.path
from path_settings import UNC_FILE_FOLDER, C_FILE_FOLDER

unc_data = os.path.join(UNC_FILE_FOLDER, '')

# find all days data
for file in os.listdir(unc_data):
    if file.endswith('.parquet'):
        df = pd.read_parquet(os.path.join(unc_data, file))
        if file.endswith('.parquet'):
            date = df.loc[0:0, 'tpep_pickup_datetime'].values.astype(str)
            date = date[0].split('-')
            year, month = int(date[0]), int(date[1])
            num_days = monthrange(year, month)
            for day in range(2, num_days[1]+1):
                df = df[df.tpep_dropoff_datetime.dt.date ==
                        dt.date(int(year), int(month), day)]
                file_name = os.path.join(
                    unc_data, 'yellow_tripdata_{}-{}-{}.parquet'.format(int(year), int(month), day))
                df.to_parquet(file_name, engine='fastparquet')
