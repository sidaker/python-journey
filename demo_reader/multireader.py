import os
import sys
from demo_reader.compressed import gzipped, bzipped
#from compressed import gzipped, bzipped
## python -m demo_reader.compressed.bzipped test.bz2 data compressed with bz2 babumush
## python -m demo_reader.compressed.gzipped test.gz data compressed with gzip babumush
## python -m demoreader.

'''
from demo_reader.multireader import MultiReader
r = MultiReader('test.bz2')
r.read()
'''

##print(sys.path)
##print(__file__)
## /Users/sbommireddy/Documents/python/python-journey/modules_packages/python-journey/demo_reader/multireader.py
### /Users/sbommireddy/Documents/python/python-journey/modules_packages/python-journey/demo_reader/compressed/bzipped.py
ext_map = {
    '.bz2': bzipped.opener,
    '.gz': gzipped.opener
}
class MultiReader:
    def __init__(self,filename):
        #extension =  os.path.split(filename)[1]
        extension =  os.path.splitext(filename)[1]
        opener = ext_map.get(extension,open)
        #print(opener)
        self.filename = filename
        self.f = opener(filename, 'rt') ## open in text mode


    def close(self):
        self.f.close()

    def read(self):
        ''' read entire file contents as a string'''
        return self.f.read()

if __name__ == '__main__':
    r = MultiReader('/Users/sbommireddy/Documents/python/python-journey/modules_packages/python-journey/test.bz2')
    print(r.read())
    r.close()
    rt = MultiReader('/Users/sbommireddy/Documents/python/python-journey/modules_packages/python-journey/demo_reader/__init__.py')
    print(rt.read())
    rt.close()
    rg = MultiReader('/Users/sbommireddy/Documents/python/python-journey/modules_packages/python-journey/test.gz')
    try:
        print(rg.read())
    except UnicodeDecodeError:
        print("Decode error")
    except:
        print("Cannot decode file")
    rg.close()
