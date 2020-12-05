highest_seat_id = 0
seat_ids = []

file = open("Day5.txt", "r")
for line in file:
    column = 0
    row = 0
    if line[0] == "B":
        row = row + 64
    if line[1] == "B":
        row = row + 32
    if line[2] == "B":
        row = row + 16
    if line[3] == "B":
        row = row + 8
    if line[4] == "B":
        row = row + 4
    if line[5] == "B":
        row = row + 2
    if line[6] == "B":
        row = row + 1
    if line[7] == "R":
        column = column + 4
    if line[8] == "R":
        column = column + 2
    if line[9] == "R":
        column = column + 1
    seat_id = ((row * 8) + column)
    seat_ids.append(seat_id)
    if seat_id > highest_seat_id:
        highest_seat_id = seat_id

def find_missing_seat(list):
    return [seat for seat in range(list[0], list[-1]+1) if seat not in list]
seat_ids.sort()

print("Highest Seat ID: ", highest_seat_id)
print("Your seat ID is: ", find_missing_seat(seat_ids))
