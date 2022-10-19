from wget import download
from posixpath import basename
from urllib import parse
import sys

URL = input('File URL: ')

path = parse.urlsplit(URL).path
domain = parse.urlparse(URL).netloc
filename = basename(path)

print(f"\nDownloading... | {filename} | From - {domain}")
response = download(URL, filename)
input("\n\nDownload complete! Press Enter to close this window.\n")

sys.exit()
