def longest_increasing_subsequence(nums):
    longest_lst = list()
    def helper(i, current_lst):
        # nonlocal longest_lst
        if len(current_lst) >= len(longest_lst):
            # longest_lst = current_lst[:]
            longest_lst.clear()
            longest_lst.extend(current_lst[:])

        if i >= len(nums):
            return

        if current_lst and current_lst[-1] > nums[i]:
            return

        # add the nums[i]
        helper(i + 1, current_lst[:] + [nums[i]])

        # not add nums[i]
        helper(i + 1, current_lst[:])

    helper(0, list())
    return longest_lst


nums = [6, 37, 2, 4, 18, 7]
print(longest_increasing_subsequence(nums))  # 2, 4, 18
