import pandas as pd
import time
from helper.generate_rhythm import generate_rhythm
from helper.generate_velocity import generate_velocity
from helper.generate_pitch import generate_pitch
from pythonosc.udp_client import SimpleUDPClient

client = SimpleUDPClient("127.0.0.1", 6666)

ride_df = pd.read_csv('./data/ride1.csv')

for row in ride_df:
    pm1 = row['PM1.0']
    pm2_5 = row['PM2.5']
    pm10 = row['PM10.0']

    #generate pitch
    pitch = generate_pitch(pm1)

    #generate velocity
    velocity = generate_velocity(pm2_5)

    #generate rhythm
    rhythm = generate_rhythm(pm10)

    client.send_message("/voice", [pitch, velocity, rhythm])
    time.sleep(1)

