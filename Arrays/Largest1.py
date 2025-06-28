nums = [10, 20, 4, 45, 99]

# Solution
max_num = nums[0]
for num in nums:
    if num > max_num:
        max_num = num

print("Largest number:", max_num)
