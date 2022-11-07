import pandas as pd
import datetime as dt
from calendar import monthrange
import os

data = pd.read_parquet('yellow_tripdata_2020-01.parquet', engine='fastparquet')

for col in data.columns:
    print('Column Name: ', col)


# print(data.tpep_dropoff_datetime)

# # find single day data
# data = data[data.tpep_dropoff_datetime.dt.date == dt.date(2020, 1, 1)]
# data.to_parquet('yellow_tripdata_2020-01-01.parquet', engine='fastparquet')
# num_days = monthrange(2020, 1)

# # find all days data
# for i in range(2, num_days[1]+1):
#     data = pd.read_parquet(
#         'yellow_tripdata_2020-01.parquet', engine='fastparquet')
#     data = data[data.tpep_dropoff_datetime.dt.date == dt.date(2020, 1, i)]
#     data.to_parquet(
#         'yellow_tripdata_2020-01-0{}.parquet'.format(i), engine='fastparquet')


# df = pd.read_parquet('yellow_tripdata_2020-01-01.parquet',
#                      engine='fastparquet')
# df = df.reset_index(drop=True)
# print(df.head())

# # create database with names
# conn = sqlite3.connect('database.sqlite')
# query = f' Create table if not exists yellow_tripdata_2020_01_05 ( VendorID integer, tpep_pickup_datetime text, tpep_dropoff_datetime text, passenger_count integer, trip_distance real, RatecodeID integer, store_and_fwd_flag text, PULocationID integer, DOLocationID integer, payment_type integer, fare_amount real, extra real, mta_tax real, tip_amount real, tolls_amount real, improvement_surcharge real, total_amount real)'
# conn.execute(query)

# df = df.reset_index(drop=True)
# df.to_sql('yellow_tripdata_2020-01-01', conn, if_exists='append', index=False)
# conn.commit()
# conn.close()


# # instert data into database
# for file in os.listdir():
#     if file.endswith('.parquet'):
#         df = pd.read_parquet(file, engine='fastparquet')
#         conn = sqlite3.connect('database.sqlite')
#         df = df.reset_index(drop=True)
#         df.to_sql(file[:-8], conn, if_exists='append', index=False)
#         conn.commit()
#         conn.close()
