from src.utils.chunking import chunk_text
from src.retriever.faiss_retriever import FaissRetriever
from src.generator.base import BaseGenerator
import os

class DummyGenerator(BaseGenerator):
    def generate(self, query, context_docs):
        return f"Answer to '{query}' from {len(context_docs)} docs."

def test_pipeline(monkeypatch):
    docs = ["This is a test document about AI.", "Another doc about machine learning."]
    chunks = chunk_text(docs, chunk_size=20, chunk_overlap=5)
    # Use a dummy OpenAI key for test
    monkeypatch.setenv('OPENAI_API_KEY', 'sk-test')
    retriever = FaissRetriever(chunks, openai_api_key='sk-test')
    generator = DummyGenerator()
    query = "What is AI?"
    retrieved = retriever.retrieve(query, top_k=2)
    answer = generator.generate(query, retrieved)
    assert 'Answer to' in answer
    assert 'docs' in answer 