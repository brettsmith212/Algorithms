# Time: O(log(n)) Space: O(log(n))

def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)

def binarySearchHelper(array, target, beg, end):
	if beg > end:
		return -1
	middle = (beg + end) // 2
	potentialMatch = array[middle]
	if target == potentialMatch:
		return middle
	elif target < potentialMatch:
		return binarySearchHelper(array, target, beg, middle - 1)
	else:
		return binarySearchHelper(array, target, middle + 1, end)