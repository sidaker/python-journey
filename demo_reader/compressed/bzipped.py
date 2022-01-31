import bz2
import sys

##opener = bz2.open
## returns a file like object
'''
open does not decompress during read
bz2.open decompresses file during reading

'''

opener = bz2.open
