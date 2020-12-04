angles = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
x = [0, 0, 0, 0, 0]
tree_count = [0, 0, 0, 0, 0]
row = 0
hill = open('input', 'r').read().split("\n")
for line in hill:
    for i in range(5):
        if (row % angles[i][1]) == 0:
            if (line[x[i]] == '#'):
                tree_count[i] = tree_count[i] + 1
            x[i] = ((x[i] + angles[i][0]) % 31)
    row = row + 1
print(tree_count)
answer = 1
for el in tree_count:
    answer = el * answer
print(answer)
