import math

a, b, c, d, n = [int(x) for x in input().split()]
works = [a, b, c, d]
letters = "ABCD"


def recursion(nums, pos):
    for place, num in enumerate(nums):
        if sum(nums) == num:
            return letters[place] * num

    total = 0
    for place, num in enumerate(nums):
        if num:
            nums[place] -= 1
            temp = math.factorial(sum(nums))
            for thing in nums:
                if thing:
                    temp //= math.factorial(thing)
            total += temp
            if total > pos:
                total -= temp
                return letters[place] + recursion(nums, pos - total)
            nums[place] += 1


print(recursion(works, n - 1))
