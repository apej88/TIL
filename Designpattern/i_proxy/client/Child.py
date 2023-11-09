from library.ProxyDeveloper import ProxyDeveloper
from library.Developer import Developer

class Child(Developer):
    def __new__(cls):
        return ProxyDeveloper(super().__new__(cls))
    
    def develop(self):
        print('자바로 개발한다')
       
        