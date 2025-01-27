import random
from img_classes.Fashion_MNIST.Fashion_MNIST import Fashion_MNIST
from img_classes.edge_cases import edge_cases
DATA_TYPES = {
    'Fashion-MNIST': Fashion_MNIST,
    'NIST-KMNC': edge_cases
}


class image_loader:
    def __init__(self, path, data_type='Fashion-MNIST'):
        self._path = path
        self.paths = {}
        self._load_paths(data_type)

    def _load_paths(self, data_type):
        load_class = DATA_TYPES[data_type]
        self.paths = load_class(self._path).get_paths()

    def get_image_set(self, size=None):
        if not size:
            size = len(self.paths.keys())
        return_list = []
        for _ in range(size):
            random.seed()
            selected_class_idx = random.randint(0, len(self.paths.keys()))
            selected_class = list(self.paths.keys())[selected_class_idx]
            selected_case_idx = random.randint(0, len(self.paths[selected_class]))
            selected_case = list(self.paths[selected_class])[selected_case_idx]
            temp_dict = {
                'class_idx': selected_class_idx,
                'case_idx': selected_case_idx,
                'class': selected_class,
                'path': selected_case
            }
            return_list.append(temp_dict.copy())
        return return_list

    def get_classes(self):
        return list(self.paths.keys())


if __name__ == '__main__':
    loader = image_loader('data/Fashion-MNIST')
    print(loader.get_image_set(5))
