def quantum_signal(n):
    
    if n == 0 or n == 1:
        return n
    
    if n % 2 == 0:
        return quantum_signal(n // 2) ^ n
    else: 
        return quantum_signal(n - 1) & n

print(quantum_signal(int(input())))
    
