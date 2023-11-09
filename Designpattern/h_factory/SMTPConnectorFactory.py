from DaumConnector import DaumConnector
from conf.EmailConfig import EmailConfig
from NaverConnector import NaverConnector
from GmailConnector import GmailConnector


class SMTPConnectorFactory:
    
    @staticmethod
    def create(mail):
        connectors = {
            'DAUM':DaumConnector(EmailConfig.DAUM_CONFIG),
            'NAVER':NaverConnector(EmailConfig.DAUM_CONFIG),
            'GMAIL':GmailConnector(EmailConfig.DAUM_CONFIG),
        }
        
        return connectors.get(mail)
    