# ADS - HW #1

## Count Divisible

Given an integer array nums and an integer k (where k >= 1), count how many numbers in the array are divisible by k.

```python
nums = [1,2,3,4,5,6,7,8,9,10], k = 2 -> 5
```

Remember that a number A is divisible by another number B if B divides A evenly. So 10 is divisible by 1, 2, 5, and 10.

```python
def count_divisible(nums, k):
  factor_count = 0

  for num in nums:
    if num % k == 0:
      factor_count += 1

  return factor_count


# print(count_divisible([1,2,3,4,5], 2))
```

## Circular Shift

Given an integer array nums and an non-negative integer k, circularly shift the array to the left by k spaces. Elements at the beginning of the array will be shifted to the end of the array.

```python
nums = [1,2,3,4,5], k = 1 -> [2,3,4,5,1]
nums = [1,2,3,4,5], k = 3 -> [4,5,1,2,3]
```

Solve the problem in-place, using only O(1) extra space. That is, you should actually manipulate the input list nums within the circular_shift method instead of returning a new list (you don't have to return anything). The unit tests will fail if you don't modify nums or if you use the assignment operator (=) to change its value.

```python
def circular_shift(nums, k):
  if not nums:  # empty list
    return

  n = len(nums)
  for i in range(k):  # run 'k' shifts
    shift_num = nums[0]  # save the first num

    for j in range(0, n - 1):  # shift nums [1, n] to left 1
      nums[j] = nums[j + 1]

    nums[-1] = shift_num  # place saved num at then end

# [1,2,3,4,5]
# [2,3,4,5,1]
# [3,4,5,1,2]
# [4,5,1,2,3]
# nums = [1,2,3,4,5]
# circular_shift(nums, 3)
# print(nums)

'''
This approach swaps around the values into the final position using arithmetic and some pivoting around indeces in O(n) time and O(1) space. Here are the steps:

  1. From index 'i', we calculate it's "final position" or shifted_pos -> (i - k) % n (where '% n' ensures we stay within the length of the list).

  2. We place the number at the shifted_pos and save the number that was there (this is the next number we must shift)

  3. Then, we can move our pivot to the position we shifted to (shifted_pos) and calculate the final position for the number that was there before the shift.

*Note* we can index lists backwards using negative indeces in Python
'''
def circular_shift_2(nums, k):
  if not nums:  # empty list
    return

  n = len(nums)

  i = 0
  shifted_num = nums[0]
  for _ in range(n):
    shifted_pos = (i - k) % n

    # swap number in shifted_pos with the shifted_num
    temp = nums[shifted_pos]
    nums[shifted_pos] = shifted_num
    shifted_num = temp

    i = shifted_pos


# nums = [1, 2, 3, 4, 5]
# circular_shift(nums, 3)
# print(nums)

# [1,2,3,4,5] 1
# [1,2,1,4,5] 3
# [1,2,1,4,3] 5
# [1,5,1,4,3] 2
# [1,5,1,2,3] 4
# [4,5,1,2,3] 1
```

## Create Nums

You are given a string s that only contains the characters "I" (increase) and "D" (decrease). Let n represent the length of the string. Write a function that returns an array of integers nums that contains any permutation of [0, 1, ..., n] such that for all i = 0, ..., n-1:

If `s[i] == "I"`, then `nums[i] < nums[i+1]`

If `s[i] == "D"`, then `nums[i] > nums[i+1]`

Examples:

```python
"IDID" -> [0,4,1,3,2]
"III" -> [0,1,2,3]
"DDI" -> [3,2,0,1]
```

```python
def create_nums(s):
  if not s:
    return []

  n = len(s)
  nums = [i for i in range(n + 1)]

  i = 0
  while i < n:
    if s[i] == 'I' and nums[i] < nums[i + 1]:
      # advance i
      i += 1
    elif s[i] == 'D' and nums[i] > nums[i + 1]:
      # advance i
      i += 1
    else:
      # swap and start over
      nums[i], nums[i + 1] = nums[i + 1], nums[i]
      i = 0

  return nums


# print(create_nums("IDID"))

# DDI
# [0,1,2,4] D


# [1,0,2,3] D


# [1,2,0,3] D

# [2,1,0,3] D
# [2,1,0,3] D
# [2,1,0,3] I
```

## One Edit Away

There are three types of edits that can be performed on strings:

insert a character
remove a character
replace a character
Given two strings s1 and s2, write a function to check if they are one edit (or zero edits) away.

Examples

```python
pale, ple -> True
pales, pale -> True
pale, bale -> True (replace p with b)
pale, bae -> False
```

```python
from collections import defaultdict
'''
Completed with the help of my Mentor: Mekeih
'''


def one_edit_away(s1, s2):
  freq_map = defaultdict(
    int
  )  # Space O(1), since there are only 26 letters in the alphabet. No matter the length of either string, we will only be storing the counts of [a-z]

  # go through s1
  for letter in s1:  # O(n) time, n = length of s1
    freq_map[letter] += 1

  # go through s2
  for letter in s2:  # O(m) time, m = length of s2
    freq_map[letter] -= 1

  # print(freq_map, len(freq_map))
  differences = 0
  for letter, count in freq_map.items():  # O(1) time only 26 slots in freq_map
    differences += count
    if differences > 1 or differences < -1:
      return False

  return True

print(one_edit_away("aabb", "aacc"))  # False
print(one_edit_away("lea", "pale"))  # False
print(one_edit_away("pale", "paleee"))  # False: too long
print(one_edit_away("pale", "pale"))  # True: same word
print(one_edit_away("palee", "pale"))  # True: remove 1
print(one_edit_away("pale", "ple"))  # True: insert 1
print(one_edit_away("pale", "palee"))  # True: remove 1
print(one_edit_away("ple", 'pale'))  # True: insert 1
print(one_edit_away("pale", "bale"))  # True: replace 1
```

## Tracing

I have attached PNGs for all 4 problems.

## Time/Space Complexity

- **Count Divisible:**

  - **Space O(1)** since I only used a single variable to keep track of the number of divisible factors.
  - **Time O(n)** since I had to iterate over each number in the given list (n is size of the nums array).

- **Circular Shift:**
  - **Space O(1)** since all the shifting was done in place.
  - **Time O(n \* k)** since for everytime I shift a number to the left, I have to shift all of the elements behind it as well; naturally, this would occur 'k' times (n is size of the nums array, and k is the number of times to be shifted).
  - Note: My 2nd solution has a O(n) time and O(1) space complexities
- **Edit:**

  - **Space O(1)** since only store letters of the alphabet in the frequency map, and there is a constant (26) letters or possible values to store. i.e. even if we have a string with 1 billion letters, we only have store 26 integers (one for each letters)
  - **Time O(n + m)** since I iterate through each string once, assuming s1 has length n and s1 has length m, we iterate through m + n letters everytime we run the function

- **Create Nums:**
  - **Space O(n)** I created an array with 'n' integer numbers
  - **Time O(n^2)** everytime I perform a swap, I return to the beginning of the list; as a result, this creates a triangle sum situation. The worst case, since my nums goes from [0, n] is all "D's" meaning I have to reverse the list.

## Skill Development

- I began to comprehend the importance of truly UNDERSTANDING a problem before even trying to solve it. Often, I just want to jump straight into the code without really understanding what the question is even asking. I was able to gain this skill by attempting the problem then running into a shortcoming and saying "oh, this is what they are asking for".
- Another thing, by solving these problems, I'm beginning to understand the importance of time management. Of course, with infinite time, I could probably come up with a fully optimized solution; however, I have constrained myself to not spend too much time on a problem before looking for help. Honestly, it's important to realize that you can't always be perfect and you sometimes have to settle with a less than optimal solution.
- I think it's important to comment out what your code should be doing in a particular area before you even try to figure out how to do. When I was doing "create_nums", I came up with 2 if-else conditions that did not have any logic (just comments saying "swap and reset")
- When solving "edit", I learned about the **"defaultdict"** and how to apply it to a problem. Naturally, this is another tool in my toolbox which I will certantly consider using in the future.

## Self-Assessment and Recognition of Skill Importance

- I think I feel uncomfortable solving questions like "create_nums" because I had a difficult time understanding what was being asked.
- For me, "circular_shift" and "count_divisible" were very easy and straightfoward to solve. I'm confident in my ability to solve problems similar in the future. If I see anysort of shifting elements in place or finding factors, I will be able to solve those fairly quickly.
- I'm very proud of the fact that I was able to go back to **circular_shift** and successfully implement my initial approach. Personally, I believe it's best to come up with 'a' solution before worrying about creating THE optimal solution.
- I learned that its important to write things out as much as possible from a high level. For instance, I could have an if-else codition that's not filled in with any logic; however, just that stuctures allows me to start to think what I need to do for those two conditions.

## Guiding Questions

- When solving "circular_shift", I was trying to find a way to arithmetically shift the numbers into the final slots. However, since I needed to preserve a O(1) space complexity, I had to do the shifting in place. As a result, if I overrode a number with the number that will end up there (after the shift occurs), I lost the ability to save that number for the future. Initially, I tried swapping the values of the shifted number and the number that was there initially; nevertheless, I couldn't figure out a feasable answer in a timely manner, so I moved onto my final "brute force" approach.

- After some time, I decided to give **circular_shift** another try and try to improve on it. Thankfully, I was able to reason through it and came up with an O(n) time complexity solution. My main realization was this: **I did not have to traverse the array in order, instead, I could pivot around and decide where I go to next based on which number I shifted and the index.** Also, initially, I struggled on calculation the final position from a base index; however, in class today, I learned that I can index lists backwards (with negative indeces). So, I could literally just subtract 'k' from positions from 'i'.
  > This approach swaps around the values into the final position using arithmetic and some pivoting around indeces in O(n) time and O(1) space. Here are the steps:
  >
  > 1.  From index 'i', we calculate it's "final position" or shifted_pos -> (i - k) % n (where '% n' ensures we stay within the length of the list).

> 2.  We place the number at the shifted_pos and save the number that was there (this is the next number we must shift)

> 3.  Then, we can move our pivot to the position we shifted to (shifted_pos) and calculate the final position for the number that was there before the shift.

> _Note_ we can index lists backwards using negative indeces in Python

- When solving the "edit" question, with the help of my tutor Mekeih, he helped me realize that the problem was a lot of simpler than I originally thought: it's just a matter of "subtracting" letters and not necessairly the location of the letter. As a result, I was able to implement a frequency map for each letter of the word. I would add the letter in s1 and subtract them in s2 (this would create a "balance" of differences). If the balance was between [-1,1], then we knew the word could be modified effectively; otherwise, there was too many differences.
