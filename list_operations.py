if __name__ == '__main__':
    N = int(input())
    
    commands = []
    records = []
    for i in range(N):
        commands.append(input().split())
        
        
    
        
    for command in commands:
        if(command[0] == 'print'):
            print(records)
        elif(command[0] == 'insert'):
            records.insert(int(command[1]) , int(command[2]))
        elif(command[0] == 'append'):
            records.append(int(command[1]))
        elif(command[0] == 'remove'):
            records.remove(int(command[1]))
        elif(command[0] == 'sort'):
            records.sort()
        elif(command[0] == 'pop'):
            records.pop()
        elif(command[0] == 'reverse'):
            records.reverse()
            
    