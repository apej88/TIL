from client.connectionCreator import ConnectionCreator
from library.dao import *

if __name__ == '__main__':
    
    dao = LibrarytDAO(ConnectionCreator())
    dao.create('CREATE TABLE users (id integer primary key, name text, age integer)')
    users = [('cyy','70'),
             ('hol','60'),
             ('htg','35'),
             ('idh','40')]
    
    dao.insert_many('insert into users (name, age) values(?, ?)', users)
    print(dao.select('select * from users'))

    
    