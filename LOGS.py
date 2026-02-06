import re

logs = []
print("Enter log lines (type 'end' to stop):")

while True:
    line = input()
    if line.lower() == "end":
        break
    logs.append(line)

pattern = r'^\[ERROR\]\s(\d{4}-\d{2}-\d{2})\s\d{2}:\d{2}:\d{2}\s-\s(.+)$'

for log in logs:
    match = re.search(pattern, log)
    if match:
        date = match.group(1)
        message = match.group(2)
        print(f"{date} : {message}")
