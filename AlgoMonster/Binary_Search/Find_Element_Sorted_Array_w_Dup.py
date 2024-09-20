 def find_first_occurrence(arr: List[int], target: int) -> int:
     left,right = 0, len(arr) - 1
     first_index = -1
     while left <= right:
         mid = (left + right)//2 
         if arr[mid] < target:
             left = mid + 1
         elif arr[mid] > target:
             right = mid - 1
         else:
             first_index = mid
             right = mid - 1

     return first_index

             
