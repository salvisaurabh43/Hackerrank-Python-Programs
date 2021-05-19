import textwrap

def wrap(string, max_width):
    
    newstring=""
    
    for i in range(0,len(string),max_width):
        newstring = newstring + string[i:i+max_width] + '\n'
             
    return newstring

if __name__ == '__main__':
    string, max_width = raw_input(), int(raw_input())
    result = wrap(string, max_width)
    print result