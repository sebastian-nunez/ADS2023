'''
Complexities:
    - Time: O(n+m), where n is the length of 'original' and 'm' is the length of the 'converted'. Assuming Python converts a string to a set by iterating over every character present: if we have 'n' characters in the 'original' string, then we have to go through each of them and add them to the set. Naturally, the same applies to the 'converted' string of length 'm' (since we are not guaranteed that I will be same length as the original) Therefore, O(n) + O(m) -> O(n+m) time.

    - Space: O(1), since we are guaranteed lowercase letters and there are only 26 letters in the alphabet, we can assume we will store at MOST 52 characters (both lowercase and uppercase letters) inside the sets: this value is NOT dependent on the input size.
'''
from collections import defaultdict


def solution_question1(original, converted):
    original_set = set(original)  # Time: O(n), Space: O(1)
    converted_set = set(converted)  # Time: O(m), Space: O(1)

    # basically, we have to ensure we have 'enough' unique characters in the 'original' to map to the converted. Since, multiple characters can map to the same character, number of unique characters in the 'original' has to be at least as big (or bigger) than the 'converted'.
    return len(original_set) >= len(converted_set)  # Time: O(1)


print(solution_question1('ABBA', 'ZYYZ'))  # true
print(solution_question1('ABC', 'GZT'))  # true
print(solution_question1('ABBA', 'ZYXY'))  # false
print(solution_question1('ABBA', 'ZYGZ'))  # false
print(solution_question1('AaBb', 'wXyz'))  # true
print(solution_question1('abcd', 'aaaa'))  # true


'''
Complexities:
    - Time: O(n), where n is the length of 'original' and 'extra_char' (only has 1 extra char). Assuming Python converts a string to a set by iterating over every character present: if we have 'n' characters in the 'original' string, then we have to go through each of them and add them to the set. Since, 'extra_char' only has 1 additional character, we can assume its length is also 'n'. Therefore, O(n) + O(n) -> O(n) time.

    - Space: O(1), since we are guaranteed lowercase letters and there are only 26 letters in the alphabet, we can assume we will store at most 26 characters inside the sets (this value is NOT dependent on the input size).
'''


def solution_question2(original, extra_char):
    original_set = set(original)  # Time: O(n), Space: O(1)
    extra_char_set = set(extra_char)  # Time: O(n), Space: O(1)

    # the symmetric difference between the two sets will give you the letters that are NOT in common in both sets
    unique_char = original_set ^ extra_char_set  # Time: O(1), Space: O(1)

    return ''.join(unique_char)  # Time: O(1)


'''
This second solution uses a hashmap to keep track of the balance of letters between the two strings. When we encounter a letter in 'original' we add 1 to the balance (for that letter); however, when we encounter a letter in 'extra_char' we subtract 1 from the balance. At the end, we can iterate through the balance of letters and whichever letter has a negative balance (indicating its present in 'extra_char' but not 'original', we know its THE extra character).

This is just an additional solution, it uses O(1) Space since only 26 possible letters can be stored in the hashmap and O(n) Time to iterate through both the 'original' and 'extra_char' strings.
'''


def solution_question2_2(original, extra_char):
    balance_map = defaultdict(int)

    for letter in original:
        balance_map[letter] += 1

    for letter in extra_char:
        balance_map[letter] -= 1

    for letter, freq in balance_map.items():
        if freq < 0:
            return letter

    return ''
