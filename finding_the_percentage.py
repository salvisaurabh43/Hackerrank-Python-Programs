#{'Krishna': [67.0, 68.0, 69.0], 'Arjun': [70.0, 98.0, 63.0], 'Malika': [52.0, 56.0, 60.0]}


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    
    if(n > 1 and n < 11):
        
        for _ in range(n):
            name, *line = input().split()
            scores = list(map(float, line))
            student_marks[name] = scores
        
        query_name = input()
    
        record = student_marks[query_name]
    
        average = (record[0] + record[1] + record[2])/3
        
        print("{:.2f}".format(average))