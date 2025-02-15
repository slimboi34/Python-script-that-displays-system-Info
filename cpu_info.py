import psutil
import subprocess

def get_cpu_info():
    print(f"CPU Cores: {psutil.cpu_count(logical=False)} (Physical)")
    print(f"CPU Threads: {psutil.cpu_count(logical=True)} (Logical)")

    try:
        freq = psutil.cpu_freq()
        if freq:
            print(f"CPU Frequency: {freq.max:.2f} MHz")
        else:
            print("CPU Frequency: Not available via psutil")
    except FileNotFoundError:
        print("CPU Frequency: Could not be determined from psutil")

    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}% per core")
    print(f"Per-Core Usage: {psutil.cpu_percent(percpu=True, interval=1)}")

if __name__ == "__main__":
    get_cpu_info()
