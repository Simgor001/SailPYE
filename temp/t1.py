import os
import sys
import requests

ver = requests.get('https://j4sy8p.coding-pages.com/Version')
print(ver.text)