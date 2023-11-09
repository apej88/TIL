from client.Man import Man
from client.Woman import Woman
from client.Child import Child
from library.ProxyDeveloper import ProxyDeveloper

if __name__ == '__main__':
    man = Man()
    man.develop()
    print()

    woman = Woman()
    woman.develop()
    print()
    
    child = Child()
    child.develop()    