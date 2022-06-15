from abc import ABCMeta, abstractmethod


class Logger(metaclass=ABCMeta):

    @abstractmethod
    def message(self, message: str):
        raise NotImplementedError

    @abstractmethod
    def error(self, error_msg: str):
        raise NotImplementedError

    @abstractmethod
    def warning(self, warning_msg: str):
        raise NotImplementedError

    @abstractmethod
    def success(self, success_msg: str):
        raise NotImplementedError
