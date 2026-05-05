import configparser
import os

config = configparser.RawConfigParser()
config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'Configuration', 'config.ini')
config.read(config_path)

#config.read(".\\Configuration\\config.ini")


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
