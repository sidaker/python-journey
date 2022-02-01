import sys
def main(opener):
    #hello
    outputfile = sys.argv[1]
    all_data = sys.argv[2:]
    f = opener(outputfile,'wt')
    f.write(' '.join(all_data))
    f.close()
