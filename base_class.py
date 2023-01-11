import abc

class Base(abc.ABC):

    @abc.abstractmethod
    def generate(self, StartVar = None):
        raise NotImplemented