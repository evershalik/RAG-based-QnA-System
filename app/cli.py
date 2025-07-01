import os
import yaml
import click
from src.utils.config import load_config
from src.utils.chunking import chunk_text
from src.ingest.loader import DocumentLoader
from src.retriever.faiss_retriever import FaissRetriever
from src.generator.openai_generator import OpenAIGenerator

@click.command()
@click.option('--config', default='config.yaml', help='Path to config file.')
def main(config):
    cfg = load_config(config)
    openai_api_key = os.getenv('OPENAI_API_KEY')
    if not openai_api_key:
        raise RuntimeError('OPENAI_API_KEY environment variable not set.')

    # Ingest documents
    loader = DocumentLoader()
    sources = cfg['pipeline']['ingest']['sources']
    all_docs = []
    for src in sources:
        if os.path.exists(src) or src.startswith('http'):
            docs = loader.load(src)
            all_docs.extend(docs)
    print(f'Loaded {len(all_docs)} documents.')

    # Chunking
    chunk_size = cfg['retriever']['chunk_size']
    overlap = cfg['retriever']['overlap']
    chunks = chunk_text(all_docs, chunk_size, overlap)
    print(f'Chunked into {len(chunks)} pieces.')

    # Build retriever
    retriever = FaissRetriever(chunks, openai_api_key)
    generator = OpenAIGenerator(
        openai_api_key=openai_api_key,
        model=cfg['generator']['model'],
        temperature=cfg['generator']['temperature'],
        max_tokens=cfg['generator']['max_tokens']
    )

    print("\nAsk questions (type 'exit' to quit):")
    while True:
        query = input('> ')
        if query.strip().lower() == 'exit':
            break
        retrieved = retriever.retrieve(query, top_k=5)
        answer = generator.generate(query, retrieved)
        print(f'\nAnswer: {answer}\n')

if __name__ == '__main__':
    main() 