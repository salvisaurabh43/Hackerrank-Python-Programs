def count_substring(string, sub_string):
    
    stringlist = list(string)
    substringlist = list(sub_string)

    occurrence = 0
  

    
    if(len(string) > 0 and len(string)<= 200):
        for i in range(len(stringlist)-len(substringlist)+1):
            count = 0
            if(stringlist[i] == substringlist[0]):    
                for j in range(len(substringlist)):
                    if(substringlist[j] == stringlist[i+j]):
                        count = count + 1
                    else:
                        pass
                if(count == len(substringlist)):
                    occurrence += 1
        
            
    return occurrence

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)