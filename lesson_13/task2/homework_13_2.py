import json
import logging
import os

logging.basicConfig(level=logging.ERROR, format='%(asctime)s -%(levelname)s -%(message)s', filename='json_logs.log')


def check_json_file(file_path, file):
    try:
        with open(file_path, 'r') as file_json:
            json.load(file_json)
    except json.JSONDecodeError as er:
        logging.error(f'JSON file {file} is not valid, error {er}')


json_files = ['login.json', 'localizations_ru.json', 'localizations_en.json', 'swagger.json']

for file in json_files:
    file_path = os.path.join(os.path.dirname(__file__), file)
    check_json_file(file_path, file)
