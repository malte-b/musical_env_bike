import pandas as pd
import time
from pythonosc.udp_client import SimpleUDPClient
import os

client = SimpleUDPClient("127.0.0.1", 6667)

dirname = os.path.dirname(__file__)
DATA_FILE = os.path.join(dirname, '../data/ride1.csv')
ride_df = pd.read_csv(DATA_FILE)
sampling_rate = 10
pm1 = 0
pm2_5 = 0
pm10 = 0

def pause():
    time.sleep(randint(0,100) * .00025)

for index, row in ride_df.iterrows():
    pm1 += row['1.0']
    pm2_5 += row['2.5']
    pm10 += row['10.0']

    if index % sampling_rate == 0 and index>0: # subsample our data and take average of last 10 seconds as value

        pm1 = (pm1/sampling_rate)
        pm2_5 = (pm2_5/sampling_rate)
        pm10 = (pm10/sampling_rate)

        # amount of geiger counts is based on pm 10 (between 0 and 25, all outliers rounded to 25)
        pm10 = round(pm10)

        if pm10 > 25:
            pm10 = 25

        print("geiger counts -> ", pm10)

        # set time in seconds while geiger clicks
        sampling_time = 1
        if pm10 == 0:
            time.sleep(sampling_time)
        else:
            for click in range(0, pm10):
                client.send_message("/geiger", [0, 721, 33])
                time.sleep(sampling_time/pm10)

        # reset
        pm1 = 0
        pm2_5 = 0
        pm10 = 0
