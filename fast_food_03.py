from collections import deque

food = int(input())
orders = deque([int(x) for x in input().split()])
print(max(orders))

for index in range(len(orders)):
    if food >= orders[0]:
        current_order = orders.popleft()
        food -= current_order

    else:
        break

if orders:
    print(f"Orders left: {' '.join([str(x) for x in orders])}")

else:
    print("Orders complete")
