from io import BytesIO
import socket
from _http.HttpRequest import HttpRequest
from _http.HttpResponse import HttpResponse
from _http.HttpStatus import HttpStatus
from infra.error.NotFoundError import NotFoundError
from urls import url_mapping

class Server:
    
    def __init__(self, host, port, req_size):
        self.__host = host
        self.__port = port
        self.__req_size = req_size
    
    def start_server(self):
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind((self.__host, self.__port))
        serversocket.listen(5)
        
        while True:
            try:
                (clientsocket, address) = serversocket.accept()
                req_msg = clientsocket.recv(self.__req_size)
                
                if  str(req_msg) == 'b\'\'': 
                    clientsocket.close()
                    continue
                
                request = HttpRequest(req_msg) 
                response = HttpResponse(clientsocket)
                target = url_mapping(request, response)
                
                # urls에 등록되지 않은 리소스 요청
                if target is None:
                    raise NotFoundError(request.get_url())        
                
                body = target()
                response.add_body(body).send()
                
            except NotFoundError as e:
                    response.add_body(e.msg).set_status(HttpStatus.NOT_FOUND)   
                    response.send()
            except:
                    response.add_body('Server Error').set_status(HttpStatus.INTERNAL_SERVER_ERROR)
                    response.send()

                    
    
