def str_rev(s):
    return s[::-1]

if(__name__=='__main__'):
    assert 'hola' == str_rev('aloh')
    assert 'xob' == str_rev('box')
    print("*"*20)
    print(str_rev('apple'))
