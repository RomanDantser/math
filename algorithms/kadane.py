def max_subarray(nums):
    local_sum = 0
    global_sum = float('-inf')
    for num in nums:
        local_sum = max(num, local_sum + num)
        global_sum = max(global_sum, local_sum)
    return global_sum
