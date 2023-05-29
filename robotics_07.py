from collections import deque


def convert_str_in_seconds(str_time):
    hours, minutes, seconds = [int(x) for x in str_time.split(':')]
    return hours * 60 * 60 + minutes * 60 + seconds


def convert_seconds_in_str(seconds):
    seconds %= 24 * 60 * 60
    hours = seconds // (60 * 60)
    seconds %= (60 * 60)
    minutes = seconds // 60
    seconds %= 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


robots_data = input().split(';')
process_time_by_robot = {}
busy_until_by_robot = {}
products_deque = deque()

time = convert_str_in_seconds(input())

for robot_data in robots_data:
    robot, time_busy = robot_data.split('-')
    process_time_by_robot[robot] = int(time_busy)
    busy_until_by_robot[robot] = -1

while True:
    product = input()
    if product != 'End':
        products_deque.append(product)
    else:
        break

while products_deque:
    product = products_deque.popleft()
    time += 1
    for name, busy_until in busy_until_by_robot.items():
        if time >= busy_until:
            busy_until_by_robot[name] = time + process_time_by_robot[name]
            print(f"{name} - {product} [{convert_seconds_in_str(time)}]")
        else:
            products_deque.append(product)
            continue



