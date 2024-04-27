def binary_search(search_list, target):
    # be sure that this list is sorted
    search_list.sort()
    # or search_list = sorted(search_list)
    
    left, right = 0, len(search_list)-1
    
    while left <= right:
        mid = (left + right) // 2
            
        if search_list[mid] == target:
            return mid
        elif search_list[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
            
    return -1
            
print(binary_search([1,13,66,27,9], 27))
            