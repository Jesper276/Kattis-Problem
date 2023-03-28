daysused = 0
acSatues = 0
statues = input()
statues = int(statues)
printer = 1


while acSatues < statues:
    if printer >= statues:
        acSatues = printer
        daysused += 1
    else:
        printer = printer + printer
        daysused += 1
    
print(daysused)