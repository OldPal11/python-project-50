import os

from gendiff import generate_diff


def test_generate_diff_yaml():
    first_file = os.path.expanduser('~/python-project-50/fixtures/file1.yaml')
    second_file = os.path.expanduser('~/python-project-50/fixtures/file2.yaml')
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