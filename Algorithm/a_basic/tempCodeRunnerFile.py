def fibonachi(n):
    if n==1 or n==2: return 1
    return fibonachi(n-1) + fibonachi(n-2)
for i in range(1,11):
    print(fibonachi(i), end=' ')