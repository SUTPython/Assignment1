def find_missing_binary(n):
    expected_xor = 0
    actual_xor = 0
    
    for i in range(2**n):
        expected_xor ^= i
    
    for _ in range(2**n - 1):
        actual_xor ^= int(input().strip(), 2)
    
    return bin((expected_xor ^ actual_xor))[2:].zfill(n)

n = int(input().strip())
print(find_missing_binary(n))
