from collections import deque

water = int(input())
name = input()
people_line = deque()

while not name == "Start":
    people_line.append(name)

    name = input()

command = input()
while not command == "End":
    if command.isdigit():
        amount = int(command)
        current_name = people_line.popleft()
        if water >= amount:
            water -= amount
            print(f"{current_name} got water")
        else:
            print(f"{current_name} must wait")

    else:
        _, amount = command.split()
        water += int(amount)

    command = input()

print(f"{water} liters left")


