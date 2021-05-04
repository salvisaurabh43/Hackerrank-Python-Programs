def swap_case(s):
    
    mylist = list(s)
    answer = ""
    
    if(len(s) > 0 and len(s) <= 1000):
        for char in mylist:
            if(char.isupper()):
                answer = answer + char.lower()
            else:
                answer = answer + char.upper()
        
    return answer

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)