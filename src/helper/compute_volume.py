import numpy as np

# TODO mock this till the sequencer is ready
data = [3, 50, 2, 9, 10, 75, 17, 30, 60, 60, 7]

# here we can set the min ans max volume
# TODO ask Henrik for typical values in dB?
MIN_VOLUME = 1
MAX_VOLUME = 8

# defines how close the volume is combined to a change in data and not the previous volume
DATA_VOLUME_RATIO = 0.2

# mapping the common PM2.5 values (between 0 and 75) to min and max volume on a linear scale
def get_volume_data(data_value):
    if data_value > 75:
        return MAX_VOLUME
    return (MAX_VOLUME - MIN_VOLUME)/75 * data_value

# combining the data based volume and the previous volume for a smooth sound
def get_volume(volume_data, previous_volume):
    data_ratio = DATA_VOLUME_RATIO * volume_data
    previous_ratio = (1 - DATA_VOLUME_RATIO) * previous_volume
    return data_ratio + previous_ratio

previous_volume = 2
for value in data:
    volume_data = get_volume_data(value)
    volume = get_volume(volume_data, previous_volume)
    print(value, " -> ", volume)
    previous_volume = volume
