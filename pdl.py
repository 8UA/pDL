try:
    import requests
    import socket
    import urllib, urllib.parse, urllib.request, urllib.error
    from posixpath import basename
    from tqdm import tqdm
    from sys import argv
    from time import sleep
except ModuleNotFoundError:
    import subprocess
    print("\nModules are missing, installing requirements. (Make sure your wifi is connected)")
    subprocess.call("pip install -r requirements.txt", shell=True)
    print("Requirements installed, restart the program.")
    exit()

def download_file():
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
    
    # Write file data and update progress bar . . .
    try:
        with open(filename, 'wb') as file:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                file.write(data)
        
        progress_bar.close()

        if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
            print("Something went wrong . . .")

    except KeyboardInterrupt:
        progress_bar.close()
        print("\nKeyboardInterrupt detected, download stopped.")
        sleep(5)
        exit()

# Function to convert Bytes from file to MB, GB, etc . . .
def format_bytes(size):
    # 2**10 = 1024
    power = 2**10
    n = 0
    power_labels = {0 : '', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    return size, power_labels[n]+'B'

url = argv[1]

print("\nGetting link content . . .")

# Get link content . . .
response = requests.get(url, stream=True)

# Fetching file name, file size and hostname info . . .
filename = basename(url)
total_size_in_bytes= int(response.headers.get('content-length', 0))
block_size = 1024 # 1 Kibibyte
host = urllib.parse.urlparse(url).netloc
host_ip = socket.gethostbyname(host)

# Start download . . .
print(f"\nDownloading... | File name - {filename} | Size - {format_bytes(total_size_in_bytes)} | From - {host} ({host_ip})")
download_file()

print("\nDownload complete! The program will close soon.")
sleep(3)
exit()
