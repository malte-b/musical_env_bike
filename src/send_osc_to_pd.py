# Set up  client for testing pd patch
from pythonosc.udp_client import SimpleUDPClient

client = SimpleUDPClient("127.0.0.1", 6666)

# Send message with frequency
# client.send_message("/oscillator/frequency", 300)

# Send message with MIDI note
# client.send_message("/midi", 64)

# Send message to activate one of the 16 sound generators
# client.send_message("/select", 0)

# Send message for each voice generator with pitch, intensity and duration (in seconds)
client.send_message("/voice", [64, 122, 2.1])
