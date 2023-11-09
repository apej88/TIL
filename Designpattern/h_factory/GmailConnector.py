from AbstractSMTPConnector import AbstractSMTPConnector

class GmailConnector(AbstractSMTPConnector):
    def __init__(self, conf):
        self.conf = conf
    
    def connect(self):
        print('GMAIl SMTP 서버에 연결되었습니다.')
    