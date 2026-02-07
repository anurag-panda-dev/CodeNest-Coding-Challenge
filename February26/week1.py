def miss_num(nums):
    n = len(nums)
    e_sum = n * (n + 1) // 2
    a_sum = sum(nums)
    return e_sum - a_sum

nums = [0, 3, 1, 4]
print(f"the missing number is {miss_num(nums)}")

"""
output:

the missing number is 2
"""
