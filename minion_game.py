def minion_game(string):
    
    stuart_score = 0
    kevin_score = 0
    stuart_mainlist = []
    kevin_mainlist = []
    vowel_list = ['A' , 'E' , 'I' , 'O' , 'U']
    mylist = list(string)
    
    if(len(string) > 0 and len(string) <= 10**6):
       
        for k in range(len(mylist)):
            character = mylist[k]
            if(character in vowel_list):                #checking for vowel or consonant
                index = k                   #avoid using list.index() -> it returns index of first occurence       
                score = len(mylist) - k 
                kevin_score = kevin_score + score
                '''
                sublist = []  
                      
                for i in range(index,len(mylist)):          
                    sublist.append(mylist[i])
                    substring = ''
                    substring = substring.join(sublist)
                    kevin_mainlist.append(substring)
                '''
                                
            else:
                index = k
                score = len(mylist) - k
                stuart_score = stuart_score + score
                
                '''
                sublist = []
            
                for i in range(index,len(mylist)):
                    sublist.append(mylist[i])
                    substring = ''
                    substring = substring.join(sublist)
                    stuart_mainlist.append(substring)
     
                
        stuart_score = len(stuart_mainlist)
        kevin_score = len(kevin_mainlist)
        '''
        
        
        if(stuart_score > kevin_score):
            print("Stuart" , stuart_score)
        elif(stuart_score < kevin_score):
            print("Kevin" , kevin_score)
        else:
            print("Draw")
        

            
    # your code goes here

if __name__ == '__main__':
    s = input()
    minion_game(s)