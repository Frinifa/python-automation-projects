import psutil

cpu = psutil.cpu_percent()

memory = psutil.virtual_memory().percent

disk = psutil.disk_usage('/').percent

print("System Monitor\n")

print("CPU Usage:", cpu, "%")
print("Memory Usage:", memory, "%")
print("Disk Usage:", disk, "%")