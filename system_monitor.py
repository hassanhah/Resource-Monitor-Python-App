import psutil
import datetime
import time

# Author: Syed Hassan Ali
# Date: April 18, 2024
# Purpose: Monitor CPU, memory, and disk usage of the system

while True:
    # CPU Usage
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f'CPU Usage: {cpu_percent}%')

    # Memory Usage
    memory_info = psutil.virtual_memory()
    print(f'Memory Usage: {memory_info.percent}%')

    # Disk Usage
    disk_usage = psutil.disk_usage('/')
    print(f'Disk Usage: {disk_usage.percent}%')

    # Wait for 5 seconds before the next check
    time.sleep(5)
