


// class ListNode(var val: Int, var next: ListNode? = null)

// class Solution {
//     fun reverseKGroup(head: ListNode?, k: Int): ListNode? {
//         var newHead = head

//         var prev: ListNode? = null
//         var cur = head
//         while(cur != null)  {
//             var end = cur

//             while (end != null && end.val != " ")
//                 end = end?.next

//             if(end && end.val == " ") {
//                 if (cur == head)
//                     newHead = reverse(cur,end)
//                 else
//                     prev?.next = reverse(cur,end)
//             }

//             prev = cur
//             cur = end
//         }

//         return newHead
//     }

//     fun reverse(cur1: ListNode?, end: ListNode?): ListNode?{
//         var prev = end
//         var cur = cur1
//         while(cur != end) {
//             val temp = cur?.next
//             cur?.next = prev
//             prev = cur
//             cur = temp
//         }

//         return prev
//     }
// }

// var head = ListNode(5)
// println(list.val)

fun MutableList<Int>.swap(i: Int, j: Int) {
    val temp = this[i]
    this[i] = this[j]
    this[j] = temp
}

fun insertionSort(nums: MutableList<Int>): MutableList<Int> {
    for (i in 1 until nums.size) {
        var j = i - 1
        while (j >= 0 && nums[j+1] < nums[j]) {
            nums.swap(j, j+1)
            j -= 1
        }
    }

    return nums
}

fun bubbleSort(nums: MutableList<Int>): MutableList<Int> {
    for (i in 0 until nums.size) {
        for (j in 0 until nums.size - i - 1) {
            if (nums[j+1] < nums[j]) {
                nums.swap(j, j+1)
            }
        }
    }

    return nums
}

fun selectionSort(nums: MutableList<Int>): MutableList<Int> {
    for (i in 0 until nums.size) {
        var min_index = i
        for (j in (i+1) until nums.size) {
            if (nums[j] < nums[min_index]) {
                min_index = j
            }
        }

        nums.swap(min_index, i)
    }

    return nums
}

fun mergeSort(nums: MutableList<Int>): MutableList<Int> {
    fun merge(list1: MutableList<Int>, list2: MutableList<Int>): MutableList<Int> {
        val mergedList = mutableListOf<Int>()

        var i = 0
        var j = 0
        while (i < list1.size && j < list2.size) {
            if (list1[i] < list2[j]) {
                mergedList.add(list1[i])
                i += 1
            } else {
                mergedList.add(list2[j])
                j += 1
            }
        }

        while (i < list1.size) {
            mergedList.add(list1[i])
            i += 1
        }

        while (j < list2.size) {
            mergedList.add(list2[j])
            j += 1
        }

        return mergedList
    }

    if (nums.size <= 1) {
        return nums
    }

    val mid = nums.size / 2

    val leftHalf = mergeSort(nums.subList(0, mid))
    val rightHalf = mergeSort(nums.subList(mid, nums.size))

    return merge(leftHalf, rightHalf)
}

fun quickSort(nums: MutableList<Int>): MutableList<Int> {
    fun helper(low: Int, high: Int): MutableList<Int> {
        if (high - low + 1 <= 1)
            return nums

        val pivot = nums[high]
        var p = low
        for (i in low until high) {
            if (nums[i] < pivot) {
                nums.swap(i, p)
                p += 1
            }
        }

        nums.swap(p, high)

        helper(low, p - 1)
        helper(p + 1, high)

        return nums
    }

    return helper(0, nums.size - 1)
}

fun quickSelect(nums: MutableList<Int>, k: Int): Int {
    val k = k - 1

    fun helper(low: Int, high: Int): Int {
        val pivot = nums[high]
        var p = low
        for (i in low until high) {
            if (nums[i] < pivot) {
                nums.swap(i, p)
                p += 1
            }
        }

        nums.swap(p, high)

        when {
            p > k -> return helper(low, p - 1)
            p < k -> return helper(p + 1, high)
            else -> return nums[p]
        }
    }

    return helper(0, nums.size - 1)
}

var nums_unsorted = mutableListOf(5,4,10,13,2,3,15)

println("Insertion Sort: ${insertionSort(nums_unsorted)}")
println("Bubble Sort: ${bubbleSort(nums_unsorted)}")
println("Selection Sort: ${selectionSort(nums_unsorted)}")
println("Merge Sort: ${selectionSort(nums_unsorted)}")
println("Quick Sort: ${quickSort(nums_unsorted)}")
println("Quick Select (3rd): ${quickSelect(nums_unsorted, 3)}")
