def count_expressions(nums, target):
  if not nums:
    return 0

  def helper(i, total):
    if total == target and i > 1:
      return 1

    if total > target:
      return 0

    if i >= len(nums):
      return 0

    add = helper(i + 1, total + nums[i])
    subtract = helper(i + 1, total - nums[i])
    multiply = helper(i + 1, total * nums[i])

    return add + subtract + multiply

  return helper(1, nums[0])


# print(count_expressions([1, 2, 3], 6))
# print(count_expressions([1, 2, 5], 7))
print(count_expressions([1,2], 1))
# print(count_expressions([0,0], 0))
