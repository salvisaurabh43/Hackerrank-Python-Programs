if __name__ == '__main__':
    
  
  
    records = [ ['Harsh' , 20] , ['Beria' , 20] , ['Varun' , 19] , ['Kakunami' , 19] , ['Vikas' , 21] ]

    for i in range(len(records)):
        for j in range(i , len(records)):
            if(records[i][1] > records[j][1]):
                temp = records[i]
                records[i] = records[j]
                records[j] = temp

            if(records[i][1] == records[j][1]):
                if(records[i][0] > records[j][0]):
                    temp = records[i]
                    records[i] = records[j]
                    records[j] = temp
    
    print(records)          
                
    for sublist in records:
        sublist[1:] = sorted(sublist[1:] , reverse=True)
    
    print(records)
    for i in range(0, len(records) - 1):
        if(records[i][1] != records[i+1][1]):
            second_lowest = records[i+1][1]
            break


    if(len(records) > 1 and len(records) < 6):        
        for sublist in records:
            if(sublist[1] == second_lowest):
                print(sublist[0])

    
