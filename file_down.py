import requests
import sys



url = str(input('Enter URL: '))
r = requests.get(url, allow_redirects=True)
open('THMlogo.png', 'wb').write(r.content)

