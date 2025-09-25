# Enter the code at row 2978, column 3083.
row = 2978
col = 3083
# Calculate the position in the sequence (cantor's diagonal argument)
N = (row + col - 2) * (row + col - 1) // 2 + col

def next(n):
    return (n * 252533) % 33554393

def find_code(n):
    code = 20151125
    for _ in range(n - 1):
        code = next(code)
    return code

print(find_code(N))