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

    

    for i in range(len(records)):
        for j in range(i , len(records)):
           if(records[i][1] > records[j][1]):
                temp = records[i]
                records[i] = records[j]
                records[j] = temp
                
                
    for sublist in records:
        sublist[1:] = sorted(sublist[1:])
    
    
    for i in range(0, len(records) - 1):
        if(records[i][1] != records[i+1][1]):
            second_lowest = records[i+1][1]
            break
            
    for sublist in records:
        if(sublist[1] == second_lowest):
            print(sublist[0])

    