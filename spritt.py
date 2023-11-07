[classrooms, sprit] = input().split( )
spritNeeded  = 0

for classes in range(int(classrooms)):
    spritNeeded = spritNeeded + int(input())

if (spritNeeded <= int(sprit)):
    print("Jebb")
else:
    print("Neibb")