def kharshans_sharif(n):
    if n == 1:
        return 1  
    
    winner = kharshans_sharif(n - 1)  
    return (winner + 1) % n + 1  

n = int(input().strip())
print(kharshans_sharif(n))
