import pandas as pd
import os.path
from path_settings import UNC_FILE_FOLDER

# metrics data
# check if empty
data = os.path.join(UNC_FILE_FOLDER, '')
if len(os.listdir(data)) == 0:
    print('No files to read from')
else:
    # Print data
    for file in os.listdir(data):
        if file.endswith('.parquet'):
            df = pd.read_parquet(os.path.join(data, file))
            print('================================================')
            print('this is averange trip distance ',    round(
                df['trip_distance'].mean(), 2), 'miles')
            print('thi is averange passenger count ',
                  round(df['passenger_count'].mean(), 2))
            print('this is averange price of tottla amount ',
                  round(df['total_amount'].mean(), 2), '$')
            print('this is averange fare amount ', round(
                df['fare_amount'].mean(), 2), '$')
            print('this is averange tip amount ', round(
                df['tip_amount'].mean(), 2), '$')
            print('this is sum of tip amount ', round(
                df['tip_amount'].sum(), 2), '$')
            print('this is total amount ', round(
                df['total_amount'].sum(), 2), '$')
            print('================================================')
