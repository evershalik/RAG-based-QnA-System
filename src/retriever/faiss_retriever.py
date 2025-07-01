from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.docstore.document import Document
from typing import List

class FaissRetriever:
    def __init__(self, docs: List[str], openai_api_key: str):
        self.embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
        self.vectorstore = FAISS.from_texts(docs, self.embeddings)

    def retrieve(self, query: str, top_k: int = 5) -> List[str]:
        docs = self.vectorstore.similarity_search(query, k=top_k)
        return [doc.page_content for doc in docs] 