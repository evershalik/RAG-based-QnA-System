from src.utils.config import load_config
import os

def test_load_config(tmp_path):
    config_content = 'test_key: test_value\n'
    config_file = tmp_path / 'test_config.yaml'
    config_file.write_text(config_content)
    config = load_config(str(config_file))
    assert config['test_key'] == 'test_value' 