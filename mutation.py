def mutate_string(string, position, character):
    
    mylist = list(string)
    
    mylist[position] = character
    
    mylist = "".join(mylist) 
    
    return mylist

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)