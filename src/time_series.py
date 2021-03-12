import pandas as pd
import time
from random import randint
from helper.generate_rhythm import generate_rhythm
from helper.generate_velocity import generate_velocity
from helper.generate_pitch import generate_pitch
from helper.generate_chord import generate_chord
from pythonosc.udp_client import SimpleUDPClient

client = SimpleUDPClient("127.0.0.1", 6666)

DATA_FILE = '../data/ride1.csv'
ride_df = pd.read_csv(DATA_FILE)
sampling_rate = 10
pm1 = 0
pm2_5 = 0
pm10 = 0

def pause():
    time.sleep(randint(0,100) * .0005)

for index, row in ride_df.iterrows():
    pm1 += row['1.0']
    pm2_5 += row['2.5']
    pm10 += row['10.0']
    if index % sampling_rate == 0 and index>0: # subsample our data and take average of last 10 seconds as value
        pm1 = (pm1/sampling_rate)*2  # make the pitches more different
        pm2_5 = (pm2_5/sampling_rate)
        pm10 = (pm10/sampling_rate)
       
        #generate pitch
        pitch = generate_pitch(pm1)
        #pitch = 64

        #generate chord
        chord = generate_chord(int(pm1),pm2_5,pm10)

        #generate velocity
        velocity = generate_velocity(pm2_5)

        #generate rhythm
        rhythm = generate_rhythm(pm10)
        #rhythm = [1]

        print([chord, velocity, rhythm])

        '''
        for note_length in rhythm:
            client.send_message("/voice", [pitch, velocity, note_length - 0.1])
            time.sleep(note_length)
        '''
        for note_length in rhythm:
            for i,note in enumerate(chord):
                client.send_message("/voice"+str(i), [note, generate_velocity(pm2_5), note_length])
                pause()
            time.sleep(note_length)
        
        # reset
        pm1 = 0
        pm2_5 = 0
        pm10 = 0
