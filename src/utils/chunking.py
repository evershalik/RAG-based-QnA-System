from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List

def chunk_text(texts: List[str], chunk_size: int = 500, chunk_overlap: int = 50) -> List[str]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    chunks = []
    for text in texts:
        chunks.extend(splitter.split_text(text))
    return chunks 