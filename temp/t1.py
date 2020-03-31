import os
import sys
import requests

ver = requests.get('https://github.com/Simgor-Team/img/blob/master/index.html')
print(ver.text)