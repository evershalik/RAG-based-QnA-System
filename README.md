# RAG QA System

A Retrieval-Augmented Generation (RAG) based Question Answering system.

## Features
- Document ingestion from PDFs, web pages, and text files
- Text chunking, cleaning, and embedding
- Vector indexing and similarity search
- Context-aware query processing using retrieval
- LLM-based answer generation from retrieved docs
- Optional: metadata filtering and reranking
- Configurable pipeline
- Logging and debug mode
- Test suite

## Quickstart

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Set your OpenAI API key
```bash
export OPENAI_API_KEY=sk-...
```

### 3. Add your data sources to `config.yaml`
Edit the `pipeline.ingest.sources` list to include your PDF, text, or web URLs.

### 4. Run the CLI interface
```bash
python -m app.cli --config config.yaml
```

### 5. Or use Docker
```bash
docker build -t rag-qa-system .
docker run --rm -e OPENAI_API_KEY=sk-... rag-qa-system python -m app.cli --config config.yaml
```

## Configuration
See `config.yaml` for all options (retriever, generator, pipeline, etc).