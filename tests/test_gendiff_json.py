import os
from pathlib import Path

from gendiff import generate_diff

BASE_DIR = Path(__file__).parent.parent / "fixtures"

def test_generate_diff_json():
    first_file = BASE_DIR / 'file1.json'
    second_file = BASE_DIR / 'file2.json'
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

