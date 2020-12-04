# first valid function
def check_valid(line):
    list = line.split()
    limits = [int(i) for i in list[0].split('-')]
    char = list[1][0]
    password = list[2]
    count = password.count(char)
    if ((limits[0] <= count) and (count <= limits[1])):
        return 0
    return 1

# second valid function
def check_valid2(line):
    list = line.split()
    limits = [int(i) for i in list[0].split('-')]
    char = list[1][0]
    password = list[2]
    if password[limits[0]-1] == char:
        if password[limits[1]-1] != char:
            return 0
        return 1
    if password[limits[1]-1] == char:
        return 0
    return 1

# Main function
Lines = open('input', 'r').readlines()
ans = 0
ans2 = 0
for line in Lines:
    if check_valid(line) == 0:
        ans += 1
    if check_valid2(line) == 0:
        ans2 += 1
print(ans)
print(ans2)
