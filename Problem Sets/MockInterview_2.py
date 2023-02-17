def binary_search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def find_location_in_matrix(matrix, target):  # Time: O(nlogn), Space: O(1)
    n = len(matrix)

    for row in range(n):  # O(n)
        if target >= matrix[row][0] and target <= matrix[row][-1]:
            col = binary_search(matrix[row], target)  # O(logn)

            if col != -1:
                return (row, col)

    return (-1, -1)


matrix = [[1, 24, 41, 89, 101],
          [34, 39, 45, 91, 104],
          [35, 43, 56, 93, 108],
          [46, 67, 98, 103, 112],
          [90, 99, 102, 110, 116]]

print(find_location_in_matrix(matrix, 103))  # (3,3)
print(find_location_in_matrix(matrix, 102))  # (4, 2)
print(find_location_in_matrix(matrix, 999))  # (-1, -1)
