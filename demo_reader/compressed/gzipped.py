import gzip
import sys

opener = gzip.open
## returns a file like object
'''
open does not decompress during read
gzip.open decompresses file during reading

'''
