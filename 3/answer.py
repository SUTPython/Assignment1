def count_valid_sequences(n):
    if n == 1:
        return 2
    if n == 2:
        return 4
    if n == 3:
        return 7
    return count_valid_sequences(n - 1) + count_valid_sequences(n - 2) + count_valid_sequences(n - 3)

n = int(input().strip())
print(count_valid_sequences(n))
