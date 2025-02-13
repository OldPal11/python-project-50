import os
from pathlib import Path

from gendiff import generate_diff

BASE_DIR = Path(__file__).parent / "fixtures"

def test_generate_diff_yaml():
    first_file = BASE_DIR / 'file1.yaml'
    second_file = BASE_DIR / 'file2.yaml'
    expected = '''{
    - follow: False
      host: hexlet.io
    - proxy: 123.234.53.22
    - timeout: 50
    + timeout: 20
    + verbose: True
    }'''
    
    assert (
        ' '.join(generate_diff(first_file, second_file).strip().split()) 
        == ' '.join(expected.strip().split())
    )