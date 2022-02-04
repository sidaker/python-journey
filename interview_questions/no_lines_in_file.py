
if(__name__=='__main__'):
    '''
    1.Open a  file
    2.Count and print number of lines in the file'
    '''

    fp =open("/Users/sbommireddy/Documents/python/python-journey/modules_packages/python-journey/interview_questions/no_lines_in_file.py")
    num_lines = sum(1 for line in fp)
    print(num_lines)
    fp.close()
