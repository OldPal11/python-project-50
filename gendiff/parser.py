import json
from pathlib import Path

import yaml


def parse_file(file_path):
    path = Path(file_path).expanduser()
    file_extension = path.suffix.lower()
    with path.open('r') as file:
        if file_extension == '.json':
            return json.load(file)
        if file_extension in ('.yml', '.yaml'):
            return yaml.safe_load(file)
        else:
            raise ValueError(f'Unsupported file extension: {file_extension}')