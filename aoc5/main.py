Seats = open('input', 'r').read().split("\n")
max_id = 0
min_id = 0
list = []
for seat in Seats:
    seat_id = 0
    for i in range(10):
        if seat[9-i] == 'B' or seat[9-i] == 'R':
            seat_id = seat_id + (1 << i)
    list.append(seat_id)
    if max_id < seat_id:
        max_id = seat_id
    if min_id > seat_id:
        min_id = seat_id
print("max id = " + str(max_id))
print("min id = " + str(min_id))
for id in list:
    if (id < max_id) and (id + 1) not in list:
        print("your seat = " + str(int(id + 1)))