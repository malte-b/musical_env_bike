def majorChord(root):
    chord = []
    chord.append(root)
    chord.append(root+4)
    chord.append(root+7)
    return chord


def minorChord(root):
    chord = []
    chord.append(root)
    chord.append(root+3)
    chord.append(root+7)
    return chord

def polyChord(root):
    return majorChord(root) + minorChord(root+11)

def generate_chord(pm1, pm2_5, pm10):
    if(pm2_5<25 and pm10<50):
        chord = majorChord(pm1)
        return chord
    elif(pm2_5<50 and pm10<75):
        chord = minorChord(pm1)
        return chord
    else:
        chord = polyChord(pm1)
        return chord
        