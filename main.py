numbers = list()

commands = int(input())

for _ in range(commands):
    command = input()
    if len(command) == 1:
        if command == '2':
            numbers.pop()

        elif command == '3':
            print(max(numbers))

        else:
            print(min(numbers))
    else:
        _, number = command.split()
        numbers.append(int(number))

rev = reversed(numbers)
print(x for x in rev)


