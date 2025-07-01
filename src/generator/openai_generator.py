from langchain.chat_models import ChatOpenAI
from typing import List

class OpenAIGenerator:
    def __init__(self, openai_api_key: str, model: str = 'gpt-4', temperature: float = 0.2, max_tokens: int = 512):
        self.llm = ChatOpenAI(
            openai_api_key=openai_api_key,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens
        )

    def generate(self, query: str, context_docs: List[str]) -> str:
        context = '\n'.join(context_docs)
        prompt = f"""You are a helpful assistant. Use the following context to answer the question.\n\nContext:\n{context}\n\nQuestion: {query}\nAnswer:"""
        response = self.llm.predict(prompt)
        return response 