import bz2
from demo_reader.util import writer
##from ..util import writer
## .. means parent of current import which demo_reader.
## returns a file like object
'''
open does not decompress during read
bz2.open decompresses file during reading

'''

opener = bz2.open

if __name__ == '__main__':
    ''''
    python /Users/sbommireddy/Documents/python/python-journey/modules_packages/python-journey/demo_reader/compressed/bzipped.py \
    /Users/sbommireddy/Documents/python/python-journey/modules_packages/python-journey/test_data/myfile.bz2 all my data to compress sid

    python -m demo_reader.compressed.gzipped test.gz data compressed with gzip babumush
    python -m demo_reader.compressed.bzipped test.bz2 data compressed with bz2 babumush
    '''
    writer.main(opener)
