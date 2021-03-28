import pandas as pd
import time
from random import randint
from helper.generate_rhythm import generate_rhythm
from helper.generate_velocity import generate_velocity
from helper.generate_chord import generate_chord
from pythonosc.udp_client import SimpleUDPClient
import os

client = SimpleUDPClient("127.0.0.1", 6666)

dirname = os.path.dirname(__file__)
DATA_FILE = os.path.join(dirname, '../data/ride1.csv')
ride_df = pd.read_csv(DATA_FILE)
sampling_rate = 10
pm1 = 0
pm2_5 = 0
pm10 = 0

def pause():
    time.sleep(randint(0,100) * .0002)

for index, row in ride_df.iterrows():
    pm1 += row['1.0']
    pm2_5 += row['2.5']
    pm10 += row['10.0']
    if index % sampling_rate == 0 and index>0: # subsample our data and take average of last 10 seconds as value

        pm1 = (pm1/sampling_rate)
        pm2_5 = (pm2_5/sampling_rate)
        pm10 = (pm10/sampling_rate)

        #generate chord
        chord = generate_chord(pm1,pm2_5,pm10)

        #generate velocity
        velocity = generate_velocity(pm2_5)

        #generate rhythm
        rhythm = generate_rhythm(pm10)

        print([pm1, pm2_5, pm10], " -> ", [chord, velocity, rhythm])

        for note_length in rhythm:
            for i,note in enumerate(chord):
                client.send_message("/voice"+str(i), [note, generate_velocity(pm2_5), note_length])
                pause()
            time.sleep(note_length)

        # reset
        pm1 = 0
        pm2_5 = 0
        pm10 = 0
