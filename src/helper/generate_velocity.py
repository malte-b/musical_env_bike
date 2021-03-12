from random import randint
dynamics_range = {5:16, # ppp
                  10:32, # pp 
                  15:48, # p 
                  18:64, # mp 
                  20:80, # mf 
                  25:96, # f 
                  30:112, # ff 
                  999:127} # fff

def generate_velocity(value):
    velocity_modification = randint(-15,15)
    for k, v in dynamics_range.items():
        if value <= k:
            return v+velocity_modification