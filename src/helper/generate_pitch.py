from helper.tonal import Tonal, mapping


tonal = Tonal()
midi_range = tonal.create_sorted_midi("Ionian", "C")

def generate_pitch(value):
    note = mapping(value, midi_range)
    return note

