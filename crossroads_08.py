from collections import deque

green_duration = int(input())
free_window_duration = int(input())
cars_passed = 0
cars_waiting = deque()

command = input()

while command != 'END':
    if command != 'green':
        cars_waiting.append(command)

    else:
        green_left = green_duration
        for car in cars_waiting:
            car_passing = cars_waiting.popleft()
        if green_left >= len(car_passing):
            cars_passed += 1
            green_left -= len(car_passing)
        else:
            if

    command = input()
