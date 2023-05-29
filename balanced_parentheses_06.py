expression = [str(x) for x in input()]

opening = []
balanced = True

for i in expression:
    if i in '{[(':
        opening.append(i)
    else:
        if opening:
            op = opening.pop()
            if op == '{' and i == '}' or op == '[' and i == ']' or op == '(' and i == ')':
                continue
            else:
                balanced = False
                break
        else:
            balanced = False
            break

if balanced:
    print('YES')
else:
    print('NO')
