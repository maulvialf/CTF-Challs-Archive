"""
IP Man
"""

from http.server import SimpleHTTPRequestHandler
import socketserver
import os
import threading

from scapy.all import *
from netfilterqueue import NetfilterQueue

# Create queue
os.system("iptables -A INPUT -p tcp --dport 8080 -j NFQUEUE --queue-num 1")
# Eliminate outbound unreachable messages
os.system("iptables -I OUTPUT -p icmp -m icmp --icmp-type port-unreachable -j DROP")
print("Created queue")


def run_server():
    try:
        # Define the server's port number
        PORT = 8080
        SimpleHTTPRequestHandler.index_file = "/opt/index.html"
        httpd = socketserver.ThreadingTCPServer(("", PORT), SimpleHTTPRequestHandler)
        httpd.serve_forever()
    except Exception as exc:
        print(exc)


def callback(packet):
    """
    Handles incoming packets and does some ~magic~.
    """

    # Extract the payload of the packet from NFQueue
    data = packet.get_payload()

    # Parse it with scapy
    scapy_pkt = IP(data)

    print("Got packet from %s..." % scapy_pkt[IP].src)

    if scapy_pkt[IP].id != 0x1337:
        packet.drop()
        return

    # If we're good, accept the packet.
    packet.accept()


threading.Thread(target=run_server, daemon=True).start()
nfqueue = NetfilterQueue()  # create a new NFQueue
nfqueue.bind(1, callback)  # bind callback to queue-num 1
try:
    nfqueue.run()  # run nfqueue until user shutdown
except KeyboardInterrupt:
    os.system("iptables -D INPUT -p tcp --dport 8080 -j NFQUEUE --queue-num 1")
    os.system("iptables -D OUTPUT -p icmp -m icmp --icmp-type port-unreachable -j DROP")
