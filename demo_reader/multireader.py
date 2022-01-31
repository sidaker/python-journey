import os
from demo_reader.compressed import gzipped, bzipped

## /Users/sbommireddy/Documents/python/python-journey/modules_packages/python-journey/demo_reader/multireader.py

class MultiReader:
    def __init__(self,filename):
        self.filename = filename
        self.f = open(filename, 'rt') ## open in text mode

    def close(self):
        self.f.close()

    def read(self):
        ''' read entire file contents as a string'''
        return self.f.read()
