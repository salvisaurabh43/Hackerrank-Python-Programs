# Enter your code here. Read input from STDIN. Print output to STDOUT 
from collections import Counter

number_of_shoes = input()
shoe_list = list(map(int , input().split()))
number_of_customers = int(input())
purchases = []
cost = 0
for i in range(number_of_customers):
    purchases.append(input().split())

shoes = Counter(shoe_list)
shoes_list = shoes.items()


for purchase in purchases:
    shoe_size = int(purchase[0])
    if(shoe_size in shoes.keys()):
        if(int(shoes[shoe_size]) != 0):
            shoes[shoe_size] -= 1
            cost = cost + int(purchase[1])

            
print(cost)