# ADS - HW #4

## Sort Squares

Given an array of integers sorted in non-decreasing order, return a new array containing the squares of each number sorted in non-decreasing order.

Examples:

`[-3, -2, 0, 4, 6] -> [0, 4, 9, 16, 36]
[-5, -3, 2, 3, 10] -> [4, 9, 9, 25, 100]`

For a fully efficient solution (and full credit), this must be done in O(n) time!

```python
def merge(lst1, lst2):  # Time O(n1 + n2) -> O(n), Space: O(n1 + n2) -> O(n)
  i = 0
  j = 0

  merged_lst = list() # O(n)
  while i < len(lst1) and j < len(lst2):
    if lst1[i] < lst2[j]:
      merged_lst.append(lst1[i])
      i += 1
    else:
      merged_lst.append(lst2[j])
      j += 1

  while i < len(lst1):
    merged_lst.append(lst1[i])
    i += 1

  while j < len(lst2):
    merged_lst.append(lst2[j])
    j += 1

  return merged_lst


# Note: for unit tests to pass, you must return a new array
# and nums must remain unchanged.
def sort_squares(nums): # Time: O(n), Space: O(n)
  result = [num**2 for num in nums]  # Time: O(n), Space: O(n)

  flip_index = -1
  for i in range(len(result) - 1): # Time: O(n)
    if result[i] < result[i + 1]:
      flip_index = i
      break

  # list was flipped at some point (went from decreasing to increasing)
  if flip_index != -1:
    first_half = result[:flip_index] # Space: O(n1)
    first_half.reverse() # Time: O(n1)
    second_half = result[flip_index:] # Space: O(n2)
    result = merge(first_half, second_half) # Time: O(n1 + n2) -> O(n)
  else:
    # list was NEVER flipped: was constantly decreasing -> reverse it
    result.reverse() # Time: O(n)

  return result

print(sort_squares([-3, -2, 0, 4, 6]))
print(sort_squares([-5, -3, 2, 3, 10]))
print(sort_squares([-10, -5, -3, 0, 2, 3, 10]))
print(sort_squares([2, 3, 10]))
print(sort_squares([10]))
print(sort_squares([-5, -3]))
```

## Group Sort

Given an array whose elements are only the numbers 0, 1, and 2 (repeated any number of times), sort the array. This must be done in place. Try to do it in one pass of the array using only constant space.

Examples:

`[2, 1, 1, 0, 2, 1] -> [0, 1, 1, 1, 2, 2]
[1, 1, 2, 0, 2] -> [0, 1, 1, 2, 2]`

You can try this iteratively or recursively. If recursively, feel free to write a helper method.

Note: The implications of this are very cool! Imagine objects colored red, green, and blue. We can label those colors 0, 1, and 2, respectively, and now we can sort them in place in linear time! Linear-time sorts do exist, they just have constraints, such as this case of having only 3 values.

```python
# Note: for unit tests to pass, this must be done in-place.
def group_sort(nums):
  buckets = [0, 0, 0]  # Space: O(1)

  for num in nums:  # Time: O(n)
    buckets[num] += 1

  i = 0
  for num, count in enumerate(buckets):  # Time: O(1), only 3 iterations
    for _ in range(count):  # Time: O(n), eventually i == len(nums)
        nums[i] = num
        i += 1

nums = [2, 1, 1, 0, 2, 1]
group_sort(nums)
print(nums)
```

## Tracing

Where can we find your tracing solutions?

I've attachted PDFs for all problems.

## Time/Space Complexity

### Sort Squares

- **Time:** O(n1 + n2) -> **`O(n)`**, where `n1` is the number of negative numbers in the input list, `n2` is the number of positive numbers in the input list and `n` is the total input size. Since I separate the lists into 2 halves (of size `n1` and `n2` respectively), and I merge them back together, this would take `O(n)` time since we simply have to go through `n` total elements during the merge (`n1` and `n2` form our ENTIRE sample space)
- **Space:** O(n1 + n2) -> **`O(n)`**, where `n1` is the number of negative numbers in the input list, `n2` is the number of positive numbers in the input list and `n` is the total input size. Since I **merge** the two halves (all the numbers), I need enough space to contain my entire input size in one list.

### Group Sort

- **Time:** `O(n)`, where `n` is the size of the `nums` list. Since we have to iterate through each number in the list (in order to increase the count for that number within its bucket): we end up iterating over `n` elements.
- **Space:** `O(1)` our bucket will always be `size 3`. It is _independent_ of input size.

## Skill Development

- When solving `sort_squares` I was able to apply the merge function used in merge sort in order to achieve optimal time complexity. Naturally, by creating the merge function and testing I was able to improve my ability to apply it in a later problem. Interestingly enough, I realized that I could merge two lists starting from opposite ends: one list is sorted in decreasing order and the other is sorted in increasing order.
- When solving `group_sort`, I was able to achieve a constant space complexity by modifiying the input list in place. Since the total number of element is all the buckets had to be equal to the length of the input list, I managed to keep an 'global' position where the next element had to be placed. In the future, I feel more confident in my ability to modify lists in place.

## Self-Assessment and Recognition of Skill Importance

- At this point, I feel extremly comfortable applying to bucket/counting sort to future problems. Honestly, its a really neat trick being able to translate/map _discrete categorical_ data into buckets and sort them in linear time. If I ever need to sort in linear time and have a discrete set of values, I will think of bucket sort immediately
- Of course, my ability to apply list merging has greatly improved! In the future, I will have no problem merging two sorted lists.

## Guiding Questions

- One thing that I learned through out these couple of problems was: being able to think about and write down all edge cases. For instance, I noticed that my `sort_squares` solution was not passing one the hidden test cases. As a result, I had to force myself to think: _what else could be going on that I'm missing?_ Of course, it turns out I was missing a fairly simple, yet important test case: the list contained only negative numbers (it was constantly decreasing and all I needed to do was reverse it). Frankly, the solution was quite straight foward: if I never found a `flipped_index` (the point where SQUARED list goes from decreasing to increasing [25, 4, **0**, 4, 16]), I knew the list had to be constantly decreasing _[25,16,4]_ and needed to be reversed.
