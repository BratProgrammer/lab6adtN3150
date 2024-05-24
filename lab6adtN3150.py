import re


class FormatError(Exception):
    pass


class UndoError(Exception):
    pass


class RedoError(Exception):
    pass


def is_it_car_number(string):
    mask = r'^[АВЕКМНОРСТУХ]{1}\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}$'
    return re.match(mask, string) is not None


class MyDict(dict):
    state_index = -1
    state_array = []

    def save_status(self):
        if self.state_index == len(self.state_array) - 1:
            self.state_index += 1
            self.state_array.append(self.copy())
        else:
            self.state_index += 1
            self.state_array[self.state_index] = self.copy()
            for i in range(len(self.state_array) - self.state_index - 1):
                self.state_array.pop(self.state_index + 1)

    def undo(self):
        self.state_index -= 1
        if self.state_index == -1:
            raise UndoError
        self.clear()
        for i in self.state_array[self.state_index]:
            super().__setitem__(i, self.state_array[self.state_index][i])

    def redo(self):
        self.state_index += 1
        if self.state_index >= len(self.state_array):
            raise RedoError
        self.clear()
        for i in self.state_array[self.state_index]:
            super().__setitem__(i, self.state_array[self.state_index][i])

    def __init__(self, data=None):
        super().__init__()
        if data is None:
            data = []
        for i in data:
            if type(i[1]) is not str:
                raise TypeError
            if is_it_car_number(i[1]):
                super().__setitem__(i[0], i[1])
            else:
                raise FormatError
        self.save_status()

    def __setitem__(self, key, value):
        if type(value) is not str:
            raise TypeError
        if is_it_car_number(value):
            for element in self:
                if element[0] == key:
                    element[1] = value
                    self.save_status()
                    return
            super().__setitem__(key, value)
            self.save_status()
        else:
            raise FormatError

    def pop(self, key):
        super().pop(key)
        self.save_status()

    def popitem(self):
        super().popitem()
        self.save_status()

    def __del__(self):
        self.state_array.clear()


