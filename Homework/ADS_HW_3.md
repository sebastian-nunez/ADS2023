# ADS - HW #3

## Generate Subsets

Given an integer list nums (no duplicates), return all possible subsets of nums (any order) (as lists, not sets). Your output must not contain duplicate subsets. Feel free to write a recursive helper method.

Example:

```python
nums = [1,2,3] →
       [
        [1,2,3],
        [1,2],
        [2,3],
        [1,3],
        [1],
        [2],
        [3],
        []
      ]
```

```python
def gen_subsets(nums):
  output = list()

  seen = set()
  def helper(i, subset):
    current = tuple(subset)

    if current not in seen:
      output.append(subset[:])
      seen.add(current)

    if i >= len(nums):
      return

    # include nums[i]
    helper(i + 1, subset[:] + [nums[i]])

    # not include nums[i]
    helper(i + 1, subset[:])

  helper(0, list())
  return output


# print(gen_subsets([1, 2, 3]))

# This function is just here to help you write unit tests.
# Feel free to use it, but you don't need to.
# Checks if two lists of lists contain the
# same subsets regardless of the order they appear
def same_subsets(lst1, lst2):
  if len(lst1) != len(lst2):
    return False

  set1 = set()
  for e1 in lst1:
    set1.add(tuple(sorted(e1)))

  set2 = set()

  for e2 in lst2:
    set2.add(tuple(sorted(e2)))

  return set1 == set2

# vals = [1,2,3]
# exp = [[], [1], [2], [3], [1,2], [1, 3], [2, 3], [1,2,3]]
# print(same_subsets(gen_subsets(vals), exp))
```

## Count Expressions

Given an integer array nums, and an integer target, write a function that determines how many expressions are possible which evaluate to target adding binary operators +, -, and \* between the digits in nums. Feel free to write a recursive helper method.

Note: You can ignore order of operations for this problem, just go left to right.

Examples:

```python
nums = [1, 2, 3], target = 6 → 2 (expressions: 1 + 2 + 3, 1 * 2 * 3)
nums = [1, 2, 5], target = 7 → 1 (expression: 1 * 2 + 5)
nums = [0, 0], target = 0 → 3 (expressions: 0 - 0, 0 + 0, 0 * 0)
```

```python
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


# print(count_expressions([1, 2, 3], 6)) # 2
# print(count_expressions([1, 2, 5], 7)) # 1
# print(count_expressions([1,2], 1)) # 0
# print(count_expressions([0,0], 0)) # 3

```

### Can Divide

Given an integer array nums, determine if it is possible to divide nums into two groups so that the sums of the two groups are equal. Explicit constraints: all the multiples of 5 must be in one group, and all the multiples of 3 (that are not a multiple of 5) must be in the other. Feel free to write a recursive helper method.

Examples:

```python
nums = [4, 4] → True
nums = [5, 2] → False
nums = [5, 2, 3] → True
nums = [2, 2, 2] → False
nums = [2, 4, 2] → True
nums = [5, 5] → False
nums = [3, 3] → False
nums = [5, 3, 8] → False
nums = [] → True
nums = [0] → True
```

```python
def can_divide(nums):
  if len(nums) == 0 or len(nums) == 1:
    return True

  def helper(i, group1, group2):
    if sum(group1) == sum(group2) and i == len(nums):
      return True

    if i >= len(nums):
      return False

    group1_take = False
    group2_take = False

    if nums[i] % 5 == 0: # multiples of 5 -> group1
      group1_take = helper(i + 1, group1[:] + [nums[i]], group2[:])
    elif nums[i] % 3 == 0: # multiples of 3 -> group2
      group2_take = helper(i + 1, group1[:], group2[:] + [nums[i]])
    else: # 'regular' numbers -> either group
      group1_take = helper(i + 1, group1[:] + [nums[i]], group2[:])
      group2_take = helper(i + 1, group1[:], group2[:] + [nums[i]])

    return group1_take or group2_take

  return helper(0, list(), list())

# print(can_divide([4,4])) # true
# print(can_divide([5,4])) # false
# print(can_divide([5,3, 8])) # false
# print(can_divide([3,3])) # false
```
