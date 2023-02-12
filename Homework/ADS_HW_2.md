# ADS - HW #2

## Two Sum

Given a list of integers, return the indices (as a Python set) of the two numbers that add up to a specific target. You may assume that each input will have at most one solution, and you may not use the same element twice. If there is no solution, you should return an empty set.

Example:

```python
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].
```

```python
def two_sum(nums, target):
  hashmap = dict()

  for i, num in enumerate(nums):
    complement = target - num
    if complement in hashmap:
      return set({hashmap[complement], i})
    else:
      hashmap[num] = i

  return set()


# print(two_sum([2, 7, 11, 15], 9)) # {0, 1}
# print(two_sum([2, 7, 11, 10], 17)) # {1, 3}
# print(two_sum([2, 11, 7, 15], 9)) # {0, 2}
```

## Find Unique

You are given a list of integers called nums. The numbers stored in the list appear twice except for one number, which only appears once. Write a method that finds this number.

Example:

```python
Input: [1, 4, 1, 3, 5, 5, 4]
Output: 3
```

```python
from collections import defaultdict

def find_unique(nums):
  freq_map = defaultdict(int)

  for num in nums:
    freq_map[num] += 1

  for num, count in freq_map.items():
    if count == 1:
      return num

  return 0

def find_unique_2(nums):
  set_a = set()
  set_b = set()

  for num in nums:
    if num not in set_a:
      set_a.add(num)
    else:
      set_b.add(num)

  unique_nums = set_a ^ set_b
  for unique_num in unique_nums:
    return unique_num


# print(find_unique([1, 4, 1, 3, 5, 5, 4]))
```

## Most Common Word

Given a string of words separated by spaces, find the word that appears the most in the string. Feel free to assume that there will be no ties.

Example:

```python
Input: "hello world hello hello world hi"
Ouput: "hello"
```

```python
from collections import defaultdict


def most_common_word(s):
  s_list = s.split(' ')

  freq_map = defaultdict(int) # O(n) space
  for word in s_list: # O(n) time
    freq_map[word] += 1

  greatest_freq = max(freq_map.values()) # O(n) time

  for word, count in freq_map.items(): # O(n) time
    if count == greatest_freq:
      return word

  return -1


# print(most_common_word("hello world hello hello world hi"))
```

## Keyboard Row

Given a list of words, return the words that can be typed using letters of the alphabet that appear on only one row of the American QWERTY keyboard. Your output should be a set that contains the strings. Your solution only needs to account for letters (not numbers or other characters) and should be case sensitive - both 'TOP' and 'top' can be typed using only the top row, but if they are both in the input they should be included in your result separately.

Example:

```python
Input: ["hello", "alaska", "dad", "peace"]
Output: {"alaska", "dad"}
```

```python
def keyboard_row(words_lst):
  output = set()  # O(n) space

  kb_row_1 = set({'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'})
  kb_row_2 = set({'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'})
  kb_row_3 = set({'z', 'x', 'c', 'v', 'b', 'n', 'm'})

  for word in words_lst:  # O(n) time
    word_set = set(word.lower()) # O(m) time

    if word_set.issubset(kb_row_1) or word_set.issubset(kb_row_2) or word_set.issubset(
        kb_row_3):  # O(1) time since only 26 letters in the alphabet
      output.add(word)

  return output


print(keyboard_row(["HELLO", "alaska", "dad", "peace"]))

```

## Time/Space Complexity

- **TwoSum**

  - **Space: O(n)**, where n is the length of the 'nums' list. Since I used a dictionary to store the index of each number in the list, worst case, I have to store all numbers into the hashmap if no solution is found.
  - **Time: O(n)**, where n is the length of the 'nums' list. In this approach, I iterated through each number in the list in order to look for it's corresponding 'complement' -> target - num

- **Find Unique**

  - **Space: O(n)**, where n is the number of distinct numbers in the 'nums' list. Since I'm storing the frequency/count of each number, if all numbers are distinct, I would need to store them all in the hashmap.
  - **Time: O(n)**, where n is the length of the 'nums' list. In solution, I have to iterate through the entire 'nums' list one element at a time: no matter the input, I always have to reach the end of the 'nums' list.

- **Most Common Word**

  - **Space: O(n)**, where n is the number of distinct words in the 's' list. Within a hashmap, I store the frequency of any particular word. Worst case, all words are unique and I have to store them all.
  - **Time: O(n)**, where n is the length of the 's' list. Since I have to count the number of occurences of each word within 's', with everyrun, I have to iterate through all the words and keep their frequencies within a hashmap.

- **Keyboard Row**
  - **Space: O(n)**, where n is the length of the 'words_lst' list. In order to take advantage of the constant time set operations, I have to convert all the words into sets (and store these within another array that I can iterate over).
  - **Time: O(n \* m)**, where n is the length of the 'words_lst' list, and m is the length of the longest word/sequence present. Everytime the program runs, I have to iterate through each word within the input list once and then convert it to a set. On its own, to convert a string to a set, I have to iterate through each letter of the word/sequence (so if a word has m characters, I have to iterate through m characters).

## Skill Development

- I think my ability to indentify which data structure may be best for a particular problem has improved. As of now, I understand the pros and cons of using Hashmaps vs. Hashsets; naturally, I'm able to reason through problems and decide which might be best.
- I believe I understand the in-and-outs of creating dictionary (and default dictionaries) and sets. By attenting class, I learned the syntax to initialize each and what are the methods used to work with each.
- I think an important consideration and something I have to be careful in the future is the "for X in Y" operation. For instance, if I iterate through a string it would actually take O(n); however, if I have a set or dict, it would actually be a O(1) look up. Of course, this is important to realize when anaylzing the time complexity of a problem. I learned that coverting a string to set takes O(n) (this applied to "Keyboard Row", where I had to go adjust my solution in order to have true O(n) time)

## Self-Assessment and Recognition of Skill Importance

- Currently, I feel extremly comfortable solving similar problems in the future. For the most part, once I understood each problem, I was able to come up with a solution fairly quickly while thinking how to implement it on a techincal level.
- I think I've gotten quite a lot of better at indentifying the space and time complexity of a problem. Moreover, using my understanding of the data structures we've learned, I'm able to pre-entively think about more optimal solutions and discard certain approaches. In the future, I just have to complete more practice problems in order to recognize patterns more quickly.
- In the future, I have to keep referencing the problem and question given. Naturally, I can forget what I'm trying to solve and skip over small details before I submit the final solution.

## Guiding Questions

- When solving the **"Keyboard Row"** problem, I was not quite sure what it was about. However, after stepping through the examples, I noticed it was a lot more straight foward than I imagined. Using my knowledge of distrete math, I quickly understood that all I needed to do was figure out if a word given was a subset of one of the keyboard rows. After that, it was just a matter of handling the small details within the implementation. For instance, the problem mentions how the program has to be case insensitive. At first, I wanted to iterate through all the words in the list and make them all lowercase; however, this did not work for some reason and was not optimal. At that point, I decided to include both lowercase and uppercase letters within each keyboard row set, although it worked, I thought it didn't make a lot of sense to duplicate each letter. Finally, I understood that before I converted each word to a set, I could convert it to lowercase.
- After solving **"Find Unique"**, some days later, I thought about another possible solution using **Sets**. In my head, if I had two sets containing numbers, if I wanted to find the unique numbers (numbers that are NOT in both sets), all I had to do was apply the symmetric difference (meaning 1 - {A and B}). Upon coding my solution, I realized that it does indeed work (while maintaining the same space and time complexity of my original solution). Personally, I found the solution using sets a bit less intuative than just using a HashMap to keep track of the frequency of each letter; however, it was a fun exercise to test out a connection between my theoretical understanding of sets and Discrete Math, with the application within an actual program.
