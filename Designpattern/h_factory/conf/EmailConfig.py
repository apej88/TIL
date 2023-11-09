from enum import Enum

class EmailConfig(Enum):
    NAVER_CONFIG = ('smtp.naver.com', 'mc', '123abc', 5000)
    DAUM_CONFIG = ('smtp.DAUM.com', 'mc', '123abc', 5000)    
    GMAIL_CONFIG = ('smtp.GMAIL.com', 'mc', '123abc', 5000)    
    
    def __init__(self, URL,ID,PASSWORD,TIMEOUT):
        self.URL = URL
        self.ID = ID
        self.PASSWORD = PASSWORD
        self.TIMEOUT = TIMEOUT