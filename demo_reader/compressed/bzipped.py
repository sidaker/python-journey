import bz2
import sys

##opener = bz2.open
## returns a file like object
'''
open does not decompress during read
bz2.open decompresses file during reading

'''

opener = bz2.open

if __name__ == '__main__':
    ''''
    python /Users/sbommireddy/Documents/python/python-journey/modules_packages/python-journey/demo_reader/compressed/bzipped.py \
    /Users/sbommireddy/Documents/python/python-journey/modules_packages/python-journey/test_data/myfile.bzip all my data to compress sid

    '''
    outputfile = sys.argv[1]
    all_data = sys.argv[2:]
    f = bz2.open(outputfile,'wt')
    f.write(' '.join(all_data))
    f.close()
