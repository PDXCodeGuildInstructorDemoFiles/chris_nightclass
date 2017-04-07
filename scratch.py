nums = [2314, 23412, 2, 5, 2341235213, 2]

highest = 0
indexa = None
indexb = None

list_range = list(range(len(nums)))
for n in list_range:
    if n < list_range[-1]:
        total = nums[n] * nums[n+1]
        if total > highest:
            highest = total
            indexa = n
            indexb = n + 1

print('Highest number total: {}'.format(highest))
print(nums[indexa])
print(nums[indexb])
