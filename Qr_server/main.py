from server import Server


if __name__ == '__main__':
    Server('localhost', 80, 4096).start_server()