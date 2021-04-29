if __name__ == '__main__':
    
    records = []
    second_lowest = 0
    for _ in range(int(input())):
        inner_list = []
        name = input()
        score = float(input())
        
        inner_list.append(name)
        inner_list.append(score)
        records.append(inner_list)


    #sort by occuerences and if occurences are same then sort by alphabet
    
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
            

    for i in range(0, len(records) - 1):
        if(records[i][1] != records[i+1][1]):
            second_lowest = records[i+1][1]
            break
    if(len(records) > 1 and len(records) < 6):        
        for sublist in records:
            if(sublist[1] == second_lowest):
                print(sublist[0])