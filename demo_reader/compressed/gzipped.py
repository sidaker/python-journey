import gzip
from ..util import writer
#from demo_reader.util import writer

opener = gzip.open
## returns a file like object
'''
open does not decompress during read
gzip.open decompresses file during reading

'''

if __name__ == '__main__':
    '''
    python /Users/sbommireddy/Documents/python/python-journey/modules_packages/python-journey/demo_reader/compressed/gzipped.py \
    /Users/sbommireddy/Documents/python/python-journey/modules_packages/python-journey/test_data/myfile.gz all my data to gzip compress sid

    fname = sys.argv[1]
    data = sys.argv[2:]
    f = gzip.open(fname,'wt')
    f.write(' '.join(data))

    '''

    writer.main(opener)
