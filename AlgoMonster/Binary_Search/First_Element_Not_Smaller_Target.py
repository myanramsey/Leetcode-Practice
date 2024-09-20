def first_not_smaller(arr: List[int], target: int) -> int:
    left,right = 0,len(arr) - 1
    min_index = -1 
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            min_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return min_index