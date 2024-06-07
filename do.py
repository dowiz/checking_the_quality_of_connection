from scapy.all import *


def send_icmp_packet(destination):
    packet = IP(dst=destination) / ICMP()
    reply = sr1(packet, timeout=1, verbose=0)
    time = round((reply.time - packet.sent_time) * 1000, 1)
    if reply:
        return time
    else:
        return None


destination = "8.8.8.8"
response_times = []
num_packets = 20

for _ in range(num_packets):
    reply = send_icmp_packet(destination)
    response_times.append(reply)
lost_packets = response_times.count(None)
packet_loss_percentage = int((lost_packets / num_packets) * 100)
min_time = min(response_times)
max_time = max(response_times)
avg_time = sum(response_times) / len(response_times)

print(f"Ping statistics for {destination}")
print(f"\tPackets: Sent = {num_packets}, Received = {
      num_packets - lost_packets}, Lost = {lost_packets} ({packet_loss_percentage}% loss),")
print("Approximate round trip times in milli-seconds:")
print(f"\tMinimum = {min_time}ms, Maximum = {
      max_time}ms, Average = {avg_time}ms")
