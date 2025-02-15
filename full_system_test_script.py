import psutil
import subprocess
import platform

def get_cpu_info():
    """Displays CPU cores, threads, frequency, and usage."""
    print(f"CPU Cores: {psutil.cpu_count(logical=False)} (Physical)")
    print(f"CPU Threads: {psutil.cpu_count(logical=True)} (Logical)")

    freq = None
    try:
        freq = psutil.cpu_freq()
        if freq:
            print(f"CPU Frequency: {freq.max:.2f} MHz")
        else:
            print("CPU Frequency: Not available via psutil")
    except FileNotFoundError:
        print("CPU Frequency: Could not be determined from psutil")


    if freq is None and platform.system() == "Darwin":
        try:
            output = subprocess.check_output(["sysctl", "-n", "hw.cpufrequency"]).strip()
            freq_mhz = int(output) / 1_000_000 
            print(f"CPU Frequency (macOS sysctl): {freq_mhz:.2f} MHz")
        except Exception as e:
            print(f"Could not fetch CPU frequency: {e}")

    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}% per core")
    print(f"Per-Core Usage: {psutil.cpu_percent(percpu=True, interval=1)}")

def get_memory_usage():
    """Displays a list of top processes sorted by RAM usage."""
    process_list = []

    for proc in psutil.process_iter(attrs=['pid', 'name', 'memory_info']):
        try:
            mem_info = proc.info.get('memory_info')  
            if mem_info:  
                process_list.append((proc.info['pid'], proc.info['name'], mem_info.rss))  
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue  


    process_list.sort(key=lambda x: x[2], reverse=True)

    print("\nTop 20 Memory-Consuming Processes:")
    print(f"{'PID':<10}{'Process Name':<30}{'Memory Usage (MB)':>20}")
    print("=" * 60)
    for pid, name, mem in process_list[:20]:  
        print(f"{pid:<10}{name:<30}{mem / (1024 ** 2):>20.2f}")

if __name__ == "__main__":
    print("=" * 30)
    print("SYSTEM INFORMATION")
    print("=" * 30)
    
    get_cpu_info()
    get_memory_usage()
