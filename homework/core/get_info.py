import pandas as pd
import os.path
import sys
from homework.path_settings import *

sys.path.append(os.path.join(os.path.dirname(__file__), '..\..'))

# metrics data
for file in os.listdir():
    if file.endswith('.parquet'):
        data = pd.read_parquet(
            file, engine='fastparquet')
        print('this is averange trip distance ',    round(
            data['trip_distance'].mean(), 2), 'miles')
        print('thi is averange passenger count ',
              round(data['passenger_count'].mean(), 2))
        print('this is averange price of tottla amount ',
              round(data['total_amount'].mean(), 2), '$')
        print('this is averange fare amount ', round(
            data['fare_amount'].mean(), 2), '$')
        print('this is averange tip amount ', round(
            data['tip_amount'].mean(), 2), '$')
        print('this is sum of tip amount ', round(
            data['tip_amount'].sum(), 2), '$')
        print('this is total amount ', round(
            data['total_amount'].sum(), 2), '$')
