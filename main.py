try:
    from wget import download
    import urllib, urllib.parse, urllib.request, urllib.error
    from posixpath import basename
    from time import sleep
    import sys
except ModuleNotFoundError:
    import subprocess
    print("\nModules are missing, installing requirements. (Make sure your wifi is connected)")
    subprocess.call("pip install -r requirements.txt", shell=True)
    print("Requirements installed, restart the program.")
    exit()

URL = sys.argv[1]

# Fetching file name, file size and destination domain . . .
filename = basename(URL)
filesize = urllib.request.urlopen(URL)
domain = urllib.parse.urlparse(URL).netloc

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

# Print file info & start download . . .
try:
    print(f"\nDownloading... | {filename} | Size - {format_bytes(filesize.length)} | From - {domain}")
    response = download(URL, filename)
except KeyboardInterrupt:
    print("\n\nKeyboardInterrupt detected, download stopped.")
    sleep(5)
    sys.exit()

print("\n\nDownload complete! The program will close soon.")
sleep(5)
sys.exit()
