import configparser

config = configparser.RawConfigParser()
config.read('.\\configurations\\config.ini')


class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('common properties','baseURL')
        return url

    @staticmethod
    def getUsername():
        useremail = config.get('common properties', 'username')
        return useremail

    @staticmethod
    def getPassword():
        password = config.get('common properties', 'password')
        return password