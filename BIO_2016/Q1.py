order = input()
left = (1, 0)
right = (0, 1)
fraction = (1, 1)

for item in order:
    if item == 'L':
        left = fraction
    else:
        right = fraction
    fraction = (left[0] + right[0], left[1] + right[1])

print(fraction[0], '/', fraction[1])
