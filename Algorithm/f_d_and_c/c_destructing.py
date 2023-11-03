class User:
    def __init__(self, name, age, job, hobby):
        self.name = name
        self.age = age
        self.job = job
        self.hobby = hobby
        
    def __str__(self):
        return f"name={self.name}, age={self.age} \
                , job={self.job}, hobby={self.hobby}"


def destructuring():
    a, b, c = [1,2,3]
    print(a,b,c)
    
    a,[b, c] = [1,['a','b']]
    print(a,b,c)
    
    a, _ , c = [1,'a','b']
    print(a,c)
    
    a, *mid, b = [1,2,3,4,5,6]
    print(a,mid,b)
    
    a, *_, b = [1,2,3,4,5,6]
    print(a,b)
    
    # nickname, age, hob, hobby
    #  하명도    20   강사  축구
    #  하명도    20   강사  농구
    #  하명도    20   강사  배구
    
    hmd= {  'nickName' : '하명도',
            'author':'testkim',
            'info' : {'age' : 20, 'job' : 'lecture'},
            'hobby' : ['축구','농구','배구'],
            'reg_date':'2023-11-04',
            'next':'/user/password/1'}

    res = []
    for hobby in hmd['hobby']:
        name, [age, job], hobby = [hmd['nickName'] \
                               , hmd['info'].values() \
                               , hobby]    
        res.append(User(name,age,job,hobby))
    
    for user in res:
        print(user)       
         
destructuring()