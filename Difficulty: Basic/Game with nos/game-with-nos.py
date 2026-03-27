def game_with_number(arr, n):
    result = []
    
    for i in range(n - 1):
        result.append(arr[i] ^ arr[i + 1])
    
    # last element remains same
    result.append(arr[n - 1])
    
    return result