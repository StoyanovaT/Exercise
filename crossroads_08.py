from collections import deque

green_duration = int(input())
free_window_duration = int(input())
cars_passed = 0
cars_waiting = deque()

command = input()
green_left = 0

while command != 'END':
    if command != 'green':
        cars_waiting.append(command)

    else:
        car_passing = cars_waiting.popleft()
        if green_duration >= len(car_passing):
            cars_passed += 1
        else:
            if

    command = input()
