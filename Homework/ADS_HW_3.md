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

## Tracing

Where can we find your tracing solutions?

I've attatched PDFs for each solution.

## Time/Space Complexity

### Generate Subsets

- **Time:** O(2^n) where `n` is the length of `nums`. Everytime the helper function runs, we have **2 choices**: include the current number or not include it. As a result, as the depth of recursion increases, for every level, we double the number of nodes from the previous level.
- **Space:** O(n^2) where `n` is the length of `nums`. For every recursive call, we need enough space to store a tuple containing at most `n` elements (all elements of `nums`); moreover, the maximum number of stack frames will be `n` (the subset containing all numbers present in `nums`). Naturally, if each stack frame requires `n` space and we have `n` recursive calls (at most), the space required is O(n^2).

### Count Expressions

- **Time:** O(3^n) where `n` is the length of `nums`. Everytime the helper function runs, we have **3 choices**: add, substract or multiply. As a result, as the depth of recursion increases, for every level, we **TRIPLE** the number of nodes from the previous level.
- **Space:** O(n), where `n` is the length of `nums`. At most, we have `n` stack frames (1 for every level) and each frame takes O(1) time (we only use simple variables, no lists, tuples, dicts etc).

### Can Divide

- **Time:** O(n \* 2^n)where `n` is the length of `nums`. Everytime the helper function runs, we have at most **2 choices** to make: include the current number in group1 or include it in group2. As a result, as the depth of recursion increases, for every level, we **double** the number of nodes from the previous level (at most); moreover, each recursive call takes O(n) time (to calculate the `sum(current)` -> which contains at most all numbers in present in `nums`)
- **Space:** O(n), where `n` is the length of `nums`. At most, we have `n` stack frames (1 for every level) and each frame takes O(1) time (we only use simple variables, no lists, tuples, dicts etc).

## Skill Development

- I think my ability to recognize the structure of recursive/backtracking problems has greatly improved. At the moment, I can read a problem and figure out if I'm going to need a branching structure or perhaps a helper function for backtracking problems. By solving all the class activities, I was able to get a grasp on the formula for different types of problems. For instance, if a problem requires a list containing the lists of possibilities, I know I will need a way to persist an 'output' list while working through individual possibilities.
- I learned that there will often be a few different base cases for recursive problems. For most of my problems, I indexed through an list, so, one of my base cases was making sure the current index was inbounds. However, there were individual base cases for each problem. For `count_expressions` I had to make sure the current total was equal to the target total.

## Self-Assessment and Recognition of Skill Importance

- Overall, I'm extremely comfortable solving these types of problems. Although, I think it's important to work on them on stages. For instance, when solving `can_divide` I felt extremely lost. Nevertheless, once I broke it down, it was really just a matter of accounting for 3 scenarios.
- I think I need to work on analyzing the time complexity of recursive algorithms. Naturally, they can be hard to wrap your head around. However, if I draw them out, it can be a lot of easier to vizualize and understand how they are growing.

## Guiding Questions

- I've realized that recursive problems can have different return values depending on the problem. For instance, if a problem is asking for 'count the number of times X things happens under Y conditions', it's probably best to return 1 for each successful occurence and return 0 for unfavorable events; moreover, if a problem has multiple ways/branches, I can just return the sum of each individual events. Or for a problem that requires to know if 'a' solution exists, I can just return a Boolean.
