from src.ingest.loader import BaseLoader

class DummyLoader(BaseLoader):
    def load(self, source):
        return [f"Loaded: {source}"]

def test_load():
    loader = DummyLoader()
    docs = loader.load('dummy.pdf')
    assert docs == ["Loaded: dummy.pdf"] 