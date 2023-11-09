from abc import ABCMeta, abstractmethod

from infra.error.NotFoundError import NotFoundError

class ViewResolver:
    @staticmethod
    def static_view(path):
        return ViewResolver.read_view(path[1:])
    
    @staticmethod
    def dynamic_view(path):
        path = 'templates/' + path    
        return ViewResolver.read_view(path)
        
    @staticmethod   
    def read_view(path):
        try:
            f = open(path, 'rb')
            bytes = f.read()
            return bytes
        except:
            raise NotFoundError(path + ' not found')
            
            
    
