import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir) + '/configurations/config.ini')


class ReadConfig:

    @staticmethod
    def getApplicationUrl():
        url = (config.get('commonInfo', 'base_url'))
        return url

    @staticmethod
    def getUserEmail():
        username = (config.get('commonInfo', 'email'))
        return username

    @staticmethod
    def getPassword():
        password = (config.get('commonInfo', 'password'))
        return password
