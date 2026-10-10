def two_sum(nums, target):
    checked = {}
    
    for x in range(len(nums)):
        complement = target - nums[x]
        if complement in checked:
            return [checked[complement], x]
        else:
            checked[nums[x]] = x
    return []

print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))