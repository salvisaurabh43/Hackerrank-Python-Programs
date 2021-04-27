def merge_the_tools(string, k):
    # your code goes here
   
    chunks = []
    for i in range(0 , len(string) , k):
        chunks.append(string[i:i+k])


    for chunk in chunks:
        subseq = ""
        
        for i in chunk:
            if(i in subseq):
                pass
            else:
                subseq = subseq + i
        
        print(subseq)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)