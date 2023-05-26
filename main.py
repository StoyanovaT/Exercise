numbers = list()

commands = int(input())

for _ in range(commands):
    command = input()
    if len(command) == 1 and numbers:
        if command == '2':
            numbers.pop()

        elif command == '3':
            print(max(numbers))

        else:
            print(min(numbers))
    elif len(command) >= 3:
        _, number = command.split()
        numbers.append(int(number))

rev = reversed(numbers)
for_print = ', '.join(str(x) for x in rev)
print(for_print)


