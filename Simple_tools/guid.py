'''This is a code used to remind you of early games timing and then other stuff'''


import time


print("press enter when the matchmaking starts")
x = input()
if x == "":
    x = -60
else:
    x = -10


outpost = [7, 8, 9]
runes = [3, 4, 5, 8, 9, 10]

alert_runes = "##########################################\n------RUNES-----RUNES------RUNES------RUNES\n##########################################"
alert_outpost = "##########################################\n------outpost-----outpost------outpost------outpost\n##########################################"

min = 0

while True:
    # every second x gets +1
    time.sleep(15)
    x += 30

    if x == 60:
        x = 0
        min += 1
    if min == 11:
        min = 1


    print(min)
    if min in outpost:
        print(alert_outpost)
    if min in runes:
        print(alert_runes)




