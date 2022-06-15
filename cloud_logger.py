from logger import Logger
from firebase import FireBase
from firebase import FireBase


class CloudLogger(Logger):

    def __init__(self, name: str):
        self.__BD: FireBase = FireBase(name)

    def message(self, message: str):
        self.__BD.write(message, "Mensaje")

    def error(self, error_msg: str):
        self.__BD.write(error_msg, "Error")

    def warning(self, warning_msg: str):
        self.__BD.write(warning_msg, "Warning")

    def success(self, success_msg: str):
        self.__BD.write(success_msg, "Success")
