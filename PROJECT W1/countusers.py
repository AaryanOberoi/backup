fname = "users.txt"
num_lines = 0
with open(fname, 'r') as f:
    for line in f:
        num_lines += 1
print("Number of Active Users:")
print(num_lines-5)