fun binarySearch(nums: List<Int>, target: Int): Int {
    var low = 0
    var high = nums.size - 1

    while (low <= high) {
        val mid = low + (high - low) / 2

        when {
            target > nums[mid] -> low = mid + 1
            target < nums[mid] -> high = mid - 1
            else -> return mid
        }
    }

    return -1
}

val nums_sorted = listOf(1,4,5,6,12,21,34)
println("Is 21 occurs at index ${binarySearch(nums_sorted, 21)} in $nums_sorted")
