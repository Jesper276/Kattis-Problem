number = input()
a,b,c = number.split(' ')
a = int(a)
b = int(b)
c = int(c)

orders = [c,a,b]
orders.sort()

A = orders[0] 
B = orders[1]
C = orders[2]

order = input()
NUM = []
for i in order:
    if i == "A":
        NUM.append(A) 
    if i == "B":
        NUM.append(B)
    if i == "C":
        NUM.append(C)
print(*NUM)