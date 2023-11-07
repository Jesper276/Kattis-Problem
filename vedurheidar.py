windspeed = input()
roads = input()
answers = []

for road in range(int(roads)):
    [road_name,safe_wind] = input().split( )
    if int(safe_wind) >= int(windspeed):
        answers.append(road_name + " opin")
    else:
        answers.append(road_name + " lokud")
for answer in answers:
    print(answer)