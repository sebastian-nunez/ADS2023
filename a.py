# def binary(n, k):
#     result = []
#     binary_helper(n, "", result, k)
#     return result


# def binary_helper(n: int, possible: str, lst: list, k):
#     if len(possible) == n:

#         return
#     num_ones = possible.count("1")  # pruwn the branch )stop recursing
#     if num_ones < k:
#         lst.append(possible)
#     binary_helper(n, possible + "0", lst)
#     binary_helper(n, possible + "1", lst)


# print(binary(3, 2))

def distribute_books(books, k):
  target = sum(books) / k

  def helper(i, subset):
    subset_sum = sum(subset)
    if subset_sum == target:
      print(subset)
      return 1

    if subset_sum > target:
      return 0

    if i >= len(books):
      return 0

    # read
    subset.append(books[i])
    read = helper(i + 1, subset)

    # not read
    subset.pop() # backtrack
    not_read = helper(i + 1, subset)

    return read + not_read

  num_subsets = helper(0, list())
  return num_subsets >= k


# print(distribute_books([8,15,11,20,8], 2)) # True [8, 15, 8] and [11, 20] -> 31
print(distribute_books([6,1,3,2,2,4,1,2], 3)) # True
