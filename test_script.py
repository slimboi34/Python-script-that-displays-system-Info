import psutil

# CPU Info
print(f"CPU Cores: {psutil.cpu_count(logical=False)} (Physical)")
print(f"CPU Threads: {psutil.cpu_count(logical=True)} (Logical)")

# Memory Info
ram = psutil.virtual_memory()
print(f"Total RAM: {ram.total / (1024 ** 3):.2f} GB")
print(f"Available RAM: {ram.available / (1024 ** 3):.2f} GB")

# Disk Info
disk = psutil.disk_usage('/')
print(f"Total Disk Space: {disk.total / (1024 ** 3):.2f} GB")
print(f"Free Disk Space: {disk.free / (1024 ** 3):.2f} GB")
