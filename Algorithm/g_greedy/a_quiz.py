def q1(change):
    coins = {500 :0, 100:0, 50:0, 10:0, 1:0}
    
    for coin in coins:
        coins[coin] = change // coin
        change %= coin
        
    return coins

print(q1(3465))
# {500: 6, 100: 4, 50: 1, 10: 1, 1: 5}

def q2(meetings):
    res = []
    sorted_arr = sorted(meetings, key=lambda e:e['end'])
    res.append(sorted_arr[0])
    
    for e in sorted_arr[1:]:
        if res[-1]['end'] <= e['start']:
            res.append(e)
    return res

meetings = [
      {'idx':1,'start':1, 'end':10}
     ,{'idx':2,'start':5, 'end':6}
     ,{'idx':3,'start':13,'end':15}
     ,{'idx':4,'start':14,'end':17}
     ,{'idx':5,'start':8, 'end':14}
     ,{'idx':6,'start':3, 'end':12}
    ]

print(q2(meetings))
# [ {'idx': 2, 'start': 5, 'end': 6}
# , {'idx': 5, 'start': 8, 'end': 14}
# , {'idx': 4, 'start': 14, 'end': 17}]