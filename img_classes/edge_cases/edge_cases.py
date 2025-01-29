from img_classes.img_interface import img_interface
import os
import json
SAVE_PATH = './img_classes/paths/'


class edge_cases(img_interface):
    def __init__(self, path, data_type='MNIST-KMNC'):
        self.paths = {}
        self._data_type = data_type
        self._path = path
        self.get_data()

    def get_data(self):
        if not os.path.exists(SAVE_PATH):
            os.makedirs(SAVE_PATH)
            self._create_info()
            self._save_info()
        else:
            if not os.path.exists(os.path.join(SAVE_PATH, self._data_type + '.json')):
                self._create_info()
                self._save_info()
            else:
                self._read_info()

    def get_classes(self):
        return list(self.paths.keys())

    def get_paths(self):
        return self.paths

    def _save_info(self):
        with open(os.path.join(SAVE_PATH, self._data_type + '.json'), 'w') as f:
            json.dump(self.paths, f)

    def _read_info(self):
        with open(os.path.join(SAVE_PATH, self._data_type + '.json'), 'r') as f:
            self.paths = json.load(f)

    def _create_info(self):
        for file in os.listdir(self._path):
            if file.endswith(".json"):
                file_path = os.path.join(self._path, file)
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    true_class = data['__gt_labels__'][0]['__gt_class__']
                    if true_class not in self.paths:
                        self.paths[true_class] = [file_path.replace('.json', '.png')]
                    else:
                        self.paths[true_class].append(file_path.replace('.json', '.png'))
