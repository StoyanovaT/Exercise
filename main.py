from collections import deque

numbers = deque(input().split())
reversed_numbers = numbers.reverse()

for n in range(len(numbers)):
    print(numbers.popleft(), end=' ')
