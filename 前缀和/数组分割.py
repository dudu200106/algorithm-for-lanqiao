# 数组分割是找到前后两段子数组和的差值最小

def find_min_difference(nums):
    total_sum = sum(nums)
    prefix_sum = 0
    min_diff = float('inf')

    for num in nums:
        prefix_sum += num
        diff = abs(prefix_sum - (total_sum - prefix_sum))
        min_diff = min(min_diff, diff)

    return min_diff
# 示例数组
nums = [1, 3, 5, 7, 2, 4, 6]

# 计算数组的最小差值
result = find_min_difference(nums)

print("原始数组:", nums)
print("数组分割后的最小差值:", result)