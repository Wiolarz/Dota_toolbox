import sys


text = list(open("hero_names.txt").read().split(" "))
file = open("output.txt", "w")

for i in text:
    file.write(i)
    file.write("\n")