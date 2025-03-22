def count_different_bits(a, b):

    xor_result = a ^ b
    
    count = 0
    while xor_result > 0:
        if xor_result & 1:  
            count += 1
        xor_result >>= 1 
    
    return count

a = int(input())
b = int(input())

result = count_different_bits(a, b)
print(result)
