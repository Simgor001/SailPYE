import os
import sys
import requests

ver = requests.get('http://sailpye.eace.top/Version')
print(ver.text)