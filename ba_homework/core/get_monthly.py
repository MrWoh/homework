import datetime as dt
from calendar import monthrange
import pandas as pd
import os.path
from path_settings import UNC_FILE_FOLDER

data = os.path.join(UNC_FILE_FOLDER, '')
for file in os.listdir(data):
    if file.endswith('.parquet'):
        df = pd.read_parquet(os.path.join(data, file))
        df["tpep_pickup_datetime"] = df["tpep_pickup_datetime"].values.astype(
            str)
        date_string = df["tpep_pickup_datetime"]
        pickup_date = list(map(lambda x: dt.datetime.strptime(
            x, '%Y-%d-%m %H:%M:%S.%fffffffff').strftime('%Y/%m'), df['tpep_pickup_datetime']))

print(pickup_date)
# print(date_string.dtypes)

# # find all days data
# num_days = monthrange(2020, 1)
# for i in range(2, num_days[1]+1):
#     data = pd.read_parquet(
#         'yellow_tripdata_2020-01.parquet', engine='fastparquet')
#     data = data[data.tpep_dropoff_datetime.dt.date == dt.date(2020, 1, i)]
#     data.to_parquet(
#         'yellow_tripdata_2020-01-0{}.parquet'.format(i), engine='fastparquet')
