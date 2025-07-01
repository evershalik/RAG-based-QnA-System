from abc import ABC, abstractmethod
from langchain.document_loaders import PyPDFLoader, TextLoader, WebBaseLoader
from typing import List
import os

class BaseLoader(ABC):
    @abstractmethod
    def load(self, source):
        pass 

class DocumentLoader:
    def __init__(self):
        pass

    def load(self, source: str) -> List[str]:
        ext = os.path.splitext(source)[-1].lower()
        if ext == '.pdf':
            loader = PyPDFLoader(source)
            docs = loader.load()
        elif ext in ['.txt', '.md']:
            loader = TextLoader(source)
            docs = loader.load()
        elif source.startswith('http://') or source.startswith('https://'):
            loader = WebBaseLoader(source)
            docs = loader.load()
        else:
            raise ValueError(f'Unsupported source type: {source}')
        return [doc.page_content for doc in docs] 