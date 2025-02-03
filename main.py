import psutil
import GPUtil
import time
import os

# Function to clear the screen
def clear_screen():
    # if windows: cls, if linux: clear
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    # Clear the screen
    clear_screen()
    # Heading
    print("Active System Monitor")
    print("*" * 20)

    # Get and display the CPU Usage
    cpu_usage = psutil.cpu_percent()
    print(f'CPU Usage: {cpu_usage}%')

    # Get and display the Random Access Memory Usage
    ram_usage = psutil.virtual_memory()
    print(f'Total RAM: {ram_usage.used / (1024**3):.2f} GB / {ram_usage.total / (1024**3):.2f} GB')

    # Get and display the GPU Usage
    gpus = GPUtil.getGPUs()
    for i, gpu in enumerate(gpus):
        print(f'GPU {i + 1} - {gpu.name}')
        print(f'GPU Memory Usage: {(gpu.memoryUtil * 100):.2f}%')
        print(f'GPU Memory Used: {gpu.memoryUsed} MB / {gpu.memoryTotal} MB')
        print(f'GPU Memory Free: {gpu.memoryFree} MB')
        print(f'GPU Temperature: {gpu.temperature} C')
        print(f'GPU Load: {gpu.load * 100}%')
        print()

    ## Get and display Storage Usage (optional, uncomment if needed)
    # storage_usage = psutil.disk_usage('/')
    # print(f'Storage Usage: {storage_usage.percent}% ({storage_usage.used / (1024**3):.2f} GB / {storage_usage.total / (1024**3):.2f} GB)')

    time.sleep(2)