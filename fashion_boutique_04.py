clothes_stack = [int(x) for x in input().split(' ')]
rack_capacity = int(input())

racks_used = 0
rack_status = 0

while clothes_stack:
    curr_clothes = clothes_stack.pop()

    if curr_clothes <= (rack_capacity - rack_status):
        rack_status += curr_clothes
        if rack_capacity == rack_status:
            racks_used += 1
            rack_status = 0
    else:
        racks_used += 1
        rack_status = 0
        rack_status += curr_clothes

if rack_status > 0:
    racks_used += 1

print(racks_used)