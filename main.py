from wget import download
from posixpath import basename
from urllib import parse
import urllib.request
from time import sleep
import sys

URL = sys.argv[1]

path = parse.urlsplit(URL).path
domain = parse.urlparse(URL).netloc
filename = basename(path)
filesize = urllib.request.urlopen(URL)

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

print(f"\nDownloading... | {filename} | Size - {format_bytes(filesize.length)} | From - {domain}")
response = download(URL, filename)
print("\n\nDownload complete! The program will close soon.")

sleep(5)
sys.exit()
