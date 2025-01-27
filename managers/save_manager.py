
import json


class save_manager:
    def __init__(self):
        return

    def save_to_db(self, return_data):
        pass

    def save_to_file(self, return_data):
        with open('results.jsonl', 'a') as f:
            f.write(json.dumps(return_data) + '\n')
