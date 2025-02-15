import psutil

def get_memory_usage():
    """Get a list of processes sorted by RAM usage."""
    process_list = []
    
    for proc in psutil.process_iter(attrs=['pid', 'name', 'memory_info']):
        try:
            mem_info = proc.info.get('memory_info')  
            if mem_info:  
                process_list.append((proc.info['pid'], proc.info['name'], mem_info.rss)) 
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue  

    process_list.sort(key=lambda x: x[2], reverse=True)

    print(f"{'PID':<10}{'Process Name':<30}{'Memory Usage (MB)':>20}")
    print("=" * 60)
    for pid, name, mem in process_list[:20]:  
        print(f"{pid:<10}{name:<30}{mem / (1024 ** 2):>20.2f}")

if __name__ == "__main__":
    get_memory_usage()
