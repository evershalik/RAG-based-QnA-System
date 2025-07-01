from src.generator.base import BaseGenerator

class DummyGenerator(BaseGenerator):
    def generate(self, query, context_docs):
        return f"Answer to '{query}' from {len(context_docs)} docs."

def test_generate():
    generator = DummyGenerator()
    answer = generator.generate('What is RAG?', ['doc1', 'doc2'])
    assert "Answer to 'What is RAG?'" in answer
    assert '2 docs' in answer 