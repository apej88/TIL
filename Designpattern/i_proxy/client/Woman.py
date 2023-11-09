from library.ProxyDeveloper import ProxyDeveloper
from library.Developer import Developer

class Woman(Developer):
    
    def __new__(cls):
        return ProxyDeveloper(super().__new__(cls))
    
    def develop(self):
        print('C++로 개발한다')
      
            
        