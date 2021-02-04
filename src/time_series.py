import pandas as pd
import time
from helper.generate_rhythm import generate_rhythm
from helper.generate_velocity import generate_velocity
# from helper.generate_pitch import generate_pitch
from pythonosc.udp_client import SimpleUDPClient

client = SimpleUDPClient("127.0.0.1", 6666)

DATA_FILE = '../data/ride1.csv'
ride_df = pd.read_csv(DATA_FILE)

#for row in ride_df:
for index, row in ride_df.iterrows():
    #print("test: " + str(row['1.0']))
    pm1 = row['1.0']
    pm2_5 = row['2.5']
    pm10 = row['10.0']

    #generate pitch
    # pitch = generate_pitch(pm1)
    pitch = 64

    #generate velocity
    velocity = generate_velocity(pm2_5)

    #generate rhythm
    rhythm = generate_rhythm(pm10)

    print([pitch, velocity, rhythm])

    for note_length in rhythm:
        client.send_message("/voice", [pitch, velocity, note_length])
        time.sleep(note_length)

    # we do not need that when we use time of the rhythm
    # time.sleep(1)
