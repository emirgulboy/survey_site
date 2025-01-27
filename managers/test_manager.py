import random
from managers.image_manager import image_loader
from managers.save_manager import save_manager

class test_manager:
    def __init__(self, settings, selected_data="Fashion-MNIST"):
        self.email = ""
        self.age = -1
        self.form_submitted = False
        self.dataset = selected_data
        self.settings = settings
        self.images = image_loader(self.settings[selected_data]['data_path'], selected_data)
        self.test_images = self.images.get_image_set(self.settings[selected_data]["test_size"])
        self.classes = self.images.get_classes()
        del self.images
        self._save_manager = save_manager()

    @property
    def test(self):
        random.seed()
        self._question_list = []
        for image in self.test_images:
            true_class = image['class']
            possible_classes = self.classes.copy()
            possible_classes.remove(true_class)
            possible_classes = random.sample(possible_classes, self.settings[self.dataset]["select_out_of"]-1)
            possible_classes.append(true_class)
            random.shuffle(possible_classes)
            self._question_list.append({
                "image_path": image['path'],
                'true_class': true_class,
                'possible_classes': possible_classes
            })
        return self._question_list

    def save_result(self, answers):
        self._results = self._question_list.copy()
        for i in range(len(answers)):
            answer = answers[i]
            self._results[i]['answer'] = answer
            if self._results[i]['true_class'] == answer:
                self._results[i]['correct'] = True
            else:
                self._results[i]['correct'] = False
        self._save_manager.save_to_file(self._results)
