import os
import sys
#from demo_reader.compressed import gzipped, bzipped
from compressed import gzipped, bzipped

print(sys.path)
print(__file__)
## /Users/sbommireddy/Documents/python/python-journey/modules_packages/python-journey/demo_reader/multireader.py
### /Users/sbommireddy/Documents/python/python-journey/modules_packages/python-journey/demo_reader/compressed/bzipped.py
ext_map = {
    '.bz2': bzipped.opener,
    '.gzip': gzipped.opener

}
class MultiReader:
    def __init__(self,filename):
        self.filename = filename
        self.f = open(filename, 'rt') ## open in text mode

    def close(self):
        self.f.close()

    def read(self):
        ''' read entire file contents as a string'''
        return self.f.read()
