import pytest
from src.retriever.base import BaseRetriever

class DummyRetriever(BaseRetriever):
    def retrieve(self, query, top_k=5):
        return [f'doc_{i}' for i in range(top_k)]

def test_retrieve():
    retriever = DummyRetriever()
    results = retriever.retrieve('test', top_k=3)
    assert len(results) == 3
    assert results == ['doc_0', 'doc_1', 'doc_2'] 