import img_classes.Fashion_MNIST as Fashion_MNIST
import img_classes.interfaces.img_interface as img_interface

DATA_TYPES = {
    'Fashion-MNIST': Fashion_MNIST
}


class image_loader:
    def __init__(self, path, data_type='Fashion-MNIST'):
        self._path = path
        self.paths = {}
        self._load_paths(data_type)

    def _load_paths(self, data_type):
        load_class = DATA_TYPES[data_type]
        self.paths = load_class(self._path).get_paths()


if __name__ == '__main__':
    loader = image_loader('data/paths.json')
    print(loader.paths)
