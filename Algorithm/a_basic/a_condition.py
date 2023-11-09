# 세 수 중 최대값 구하기
def max(a,b,c):
    max = a
    if(b > max):max = b
    if(c > max):max = c 
    return max

# 세 수 중 최소값 구하기
def min(a,b,c):
    min = a
    if(b < min) : min = b
    if(c < min) : min = c
    return min

# 세 수 중 중간값 구하기
def med(a, b, c):
    return a+b+c - max(a,b,c) - min(a,b,c)

print(max(55,255,30))
print(min(55,255,30))
print(med(55,255,30))