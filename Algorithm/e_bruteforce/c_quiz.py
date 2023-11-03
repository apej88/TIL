# 매개변수로 전달받은 N번째 종말의 수까지 모든 종말의 수를 담은 배열을 반환하시오
def doom_day(n):
    arr = []
    doom = 666
    cnt = 0
    
    while True:
        if '666' in str(doom):
            cnt += 1
            arr.append(doom)
        
        if cnt == n : break
        doom += 1
    
    return arr

def q2(arr):
    s = sum(arr)
    for i in range(len(arr) -1):
        for j in range(i+1, len(arr)):
            if s - (arr[i] + arr[j]) == 100:
                a, b = arr[i], arr[j]
                arr.remove(a)
                arr.remove(b)
                return arr
    
    return None     
    