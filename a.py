def binary_search_recursive(nums, target):

    def helper(lower, upper):
        if lower > upper:
            return -1

        mid = lower + (upper - lower) // 2

        if target < nums[mid]:
            return helper(lower, mid - 1)
        elif target > nums[mid]:
            return helper(mid + 1, upper)
        else:
            return mid

    return helper(0, len(nums) - 1)

print(binary_search_recursive([1,2,3,4,5], 4)) # 3
print(binary_search_recursive([1,2,3,4,5], 8)) # -1
