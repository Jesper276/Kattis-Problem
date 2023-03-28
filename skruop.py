volume = 7
n = input()

x = range(int(n))


for i in x:
    sound = input()
    if sound == "Skru op!" and volume != 10:
        volume += 1
    elif sound == "Skru ned!" and volume != 0:
        volume -= 1
print(volume)