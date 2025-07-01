import yaml
import logging

from src.utils.config import load_config

def main():
    config = load_config('config.yaml')
    logging.basicConfig(level=logging.INFO)
    logging.info('RAG QA System started.')
    print('RAG QA System is running!')
    # TODO: Add pipeline logic here

if __name__ == '__main__':
    print('Run the CLI interface with: python -m app.cli --config config.yaml') 