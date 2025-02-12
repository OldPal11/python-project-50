import json
from pathlib import Path


def parse_file(file_path):
    path = Path(file_path).expanduser()
    with path.open('r') as file:
        return json.load(file)


def generate_diff(first_file, second_file):
    first_data = parse_file(first_file)
    second_data = parse_file(second_file)
    result = []

    all_keys = sorted(set(first_data.keys()) | set(second_data.keys()))
    for key in all_keys:
        if key in first_data and key in second_data:
            if first_data[key] == second_data[key]:
                result.append(f'    {key}: {first_data[key]}')
            else:
                result.append(f'  - {key}: {first_data[key]}')
                result.append(f'  + {key}: {second_data[key]}')
        elif key in first_data:
            result.append(f'  - {key}: {first_data[key]}')
        else:
            result.append(f'  + {key}: {second_data[key]}')
        
    return '{\n' + '\n'.join(result) + '\n}'