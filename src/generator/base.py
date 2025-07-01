from abc import ABC, abstractmethod

class BaseGenerator(ABC):
    @abstractmethod
    def generate(self, query, context_docs):
        pass 