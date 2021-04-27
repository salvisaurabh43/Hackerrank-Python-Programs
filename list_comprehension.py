if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    main_list = []
    
    for i in range(0,x+1):
        for j in range(0,y+1):
            for k in range(0,z+1):
                inner_list = []
                inner_list.append(i)
                inner_list.append(j)
                inner_list.append(k)
                print(inner_list)
                main_list.append(inner_list)

    print(main_list)