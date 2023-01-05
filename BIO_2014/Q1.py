n = int(input())

lucky_numbers = [x * 2 + 1 for x in range(5100)]

count = 1
while count < len(lucky_numbers):
    num = lucky_numbers[count]
    counter = num - 1
    while counter < len(lucky_numbers):
        lucky_numbers.pop(counter)
        counter += num - 1
    count += 1

for pos, item in enumerate(lucky_numbers):
    if item > n:
        if lucky_numbers[pos - 1] == n:
            print(lucky_numbers[pos - 2], item)
        else:
            print(lucky_numbers[pos - 1], item)
        break
