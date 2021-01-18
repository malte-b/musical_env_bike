# Set up  client for testing pd patch
from pythonosc.udp_client import SimpleUDPClient

client = SimpleUDPClient("127.0.0.1", 6666)

# Send message with frequency
client.send_message("/oscillator/frequency", 300)
