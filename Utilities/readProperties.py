import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get("Common info", "base_url")
        return url

    @staticmethod
    def getUsername():
        userName = config.get("Common info", "username")
        return userName

    @staticmethod
    def getPassword():
        passsWord = config.get("Common info", "password")
        return passsWord
