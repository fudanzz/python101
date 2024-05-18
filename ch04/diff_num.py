def diff_nums(nums):
    new_set = set(nums)
    return len(new_set)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(diff_nums(nums))  # 10