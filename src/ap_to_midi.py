import mido
import time
#import json
from datadog import statsd
import traceback
import pandas as pd

from tonal import Tonal, mapping


output = mido.open_output()
tonal = Tonal()
mid_range = tonal.create_sorted_midi("HarmonicMajor", "C")
start = time.time()
max_time = 100
values = dict()
old_values = dict()

chans = dict(
    pm1=1,
    pm2_5=2,
    pm10=3
)


def get_info():
    #hourly = []
    df = pd.read_csv('../data/ride1.csv')
    #for i in range(len(r["hourly"]["data"])):
    #    hourly.append(r["hourly"]["data"][i])
    return df #hourly


def parse(record):
    values.update(pm1=record["PM1.0"])
    values.update(pm2_5=record["PM2.5"])
    values.update(pm10=record["PM10.0"])

keys = ["PM1.0", "PM2.5", "PM10.0"]

while True:
    data = get_info()
    for item in data:
        parse(item)
        print("values: {}".format(values))
        for key, value in values.items():
            chan = chans.get(key)
            print("value: {}".format(value))
            print("chan: {}".format(chan))
            note = mapping(value, mid_range)
            print("note: {}".format(note))
            try:
                output.send(mido.Message(
                    'note_on',
                    note=mapping(value, mid_range),
                    velocity=50,
                    channel=chan))
            except Exception:
                traceback.print_exc()
            time.sleep(1)
            print(key, value, "note on", chan)
            statsd.gauge(key, value)
    for item in data:
        parse(item)
        for key, value in values.iteritems():
            chan = chans.get(key)
            output.send(mido.Message(
                'note_off',
                note=mapping(value, mid_range),
                channel=chan))
            time.sleep(1)
            print(key, value, "note off", chan)