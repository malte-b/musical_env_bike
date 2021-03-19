from random import randint
dynamics_range = {15:31, # pp 
                  20:42, # p 
                  23:53, # mp 
                  25:64, # mf 
                  30:80, # f 
                  999:96} # ff 

def generate_velocity(value):
    velocity_modification = randint(-10,10)
    for k, v in dynamics_range.items():
        if value <= k:
            return v+velocity_modification