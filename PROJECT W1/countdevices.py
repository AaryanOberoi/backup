import os
os.sudo rabbitmqctl list_queues > devices.txt
fname = "devices.txt"
num_lines = 0
with open(fname, 'r') as f:
    for line in f:
        num_lines += 1
print("Number of Active Devices:")
print(num_lines-3)