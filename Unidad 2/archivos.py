file = open("devices.txt", "r")
devices = []

for line in file:
    line = line.strip()
    devices.append(line)
print(devices)
file.close()


    