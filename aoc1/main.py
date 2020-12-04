# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

file1 = open('input', 'r')
Lines = file1.readlines()

i = 0
nbrs = []
count = 0

# Strips the newline character
for line in Lines:
    for second in Lines:
        for third in Lines:
            if int(line) + int(second) + int(third) == 2020:
                print("Line{}: {}".format(count, line.strip()))
                print(int(line) * int(second) * int(third))
