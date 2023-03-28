import math

books = int(input())
price = [int(input()) for i in range(books)]
price.sort()

group = []
prices = 0

n = 3
for x in range(len(price)):
    group.append(price.pop())

    print(group)

prices += sum(group)
print(prices)

    

