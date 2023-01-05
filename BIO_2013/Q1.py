min1, min2 = [(60 + int(x)) % (60 * 24) for x in input().split()]

time1 = min1 + 60
time2 = min2 + 60

max_time = 60 * 24

while time1 != time2:
    time1 += min1 + 60
    time2 += min2 + 60
    time1 %= max_time
    time2 %= max_time

print(str(time1 // 60).zfill(2) + ':' + str(time1 % 60).zfill(2))
