C = int(input())

classes = [];

for i in range(C):
    classes.append(input().split(" "))

array2 = []
print(classes)
print(classes[0][0])
for i in range(int(classes[0][0])):
    classes[0].sort()
    print(classes[0][i+1])