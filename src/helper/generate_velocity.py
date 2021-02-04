dynamics_range = {10:16,20:32,30:48,35:64,40:80,50:96,60:112,999:127} # ppp,pp,p,mp,mf,f,ff,fff

def generate_velocity(value):
    for k, v in dynamics_range.items():
        if value <= k:
            return v