def q1(arr):
    sum_arr = [arr[0]]
    
    for e in arr[1:]:
        sum_arr.append(max(sum_arr[-1] + e, e))    
    
    return max(sum_arr)


print(q1([10, -4, 3, 1, 5, 6, -35, 12, 21, -1]))