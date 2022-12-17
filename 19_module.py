import sys 
print(sys.path)

import re
text = "Mi numero de telefono es 300 884468, el codigo del pais es 57, mi numero de la suerte 2"
result = re.findall('[0-9]+', text)
print(result)

import time
timestamp = time.time()
local = time.localtime()
result = time.asctime(local)
print(result)


import collections 
numbers = [1,1,2,1,2,2,3,3,4]
counter = collections.Counter(numbers)
print(counter)