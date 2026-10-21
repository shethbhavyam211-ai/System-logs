import sys
from collections import Counter

filename = sys.argv[1] # the first thing after the program name
position = int(sys.argv[2])
process_name = sys.argv[3]

with open(filename) as f:
    lines = f.readlines()

print("Total lines:", len(lines))

process_count = 0
counts = Counter()
for line in lines:
    fields = line.split()
    if process_name in line:
        process_count += 1
    
    if len(fields) > position:
        key = fields[position]
        counts[key] += 1

print("The count of process", process_name, "is", process_count)
print("Top 5:")
for item, n in counts.most_common(5):
    print(item, n)