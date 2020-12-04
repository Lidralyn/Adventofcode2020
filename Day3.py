first_tree = 0
second_tree = 0
third_tree = 0
forth_tree = 0
fifth_tree = 0

def slope_one():
    file = open("input.txt", "r")
    file.readline()
    global first_tree
    position = 0
    for line in file:
        position = int(position + 3)
        if position >= 31:
            position = int(position - 31)
        if line[position] == "#":
            first_tree += 1

def slope_two():
    file = open("input.txt", "r")
    file.readline()
    global second_tree
    position = 0
    for line in file:
        position = int(position + 1)
        if position >= 31:
            position = int(position - 31)
        if line[position] == "#":
            second_tree += 1

def slope_three():
    file = open("input.txt", "r")
    file.readline()
    global third_tree
    position = 0
    for line in file:
        position = int(position + 5)
        if position >= 31:
            position = int(position - 31)
        if line[position] == "#":
            third_tree += 1

def slope_four():
    file = open("input.txt", "r")
    file.readline()
    global forth_tree
    position = 0
    for line in file:
        position = int(position + 7)
        if position >= 31:
            position = int(position - 31)
        if line[position] == "#":
            forth_tree += 1

def slope_five():
    file = open("input.txt", "r")
    file.readline()
    file.readline()
    global fifth_tree
    position = 0
    for line in file:
        position = int(position + 1)
        file.readline()
        if position >= 31:
            position = int(position - 31)
        if line[position] == "#":
            fifth_tree += 1

slope_one()
slope_two()
slope_three()
slope_four()
slope_five()
total_multiplied_trees = first_tree * second_tree * third_tree * forth_tree * fifth_tree
print("The total trees hit in slope 1: ", first_tree)
print("The total trees hit in slope 2: ", second_tree)
print("The total trees hit in slope 3: ", third_tree)
print("The total trees hit in slope 4: ", forth_tree)
print("The total trees hit in slope 5: ", fifth_tree)
print("The answer for problem 2 is", total_multiplied_trees)

