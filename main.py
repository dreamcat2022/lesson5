class Shoes:
    def __init__(self, model, weight, color, size, wide):
        self.model = model
        self.weight = weight
        self.color = color
        self._size = size
        self.__wide = wide

    def hello(self):
        return f"undefined {self.color}"

    def get_size(self):
        return self._size

    def get_wide(self):
        return self.__wide

    def set_size(self, n):
        self._size = n

    def set_wide(self, w):
        self.__wide = w


class Sneakers(Shoes):
    def hello(self):
        return f"easy wearing {self.color}"


class Sandals(Shoes):
    pass


sneakers1 = Sneakers("FS", 'light', "white", 9, "ww")
sandals1 = Sandals("SF", "heavy", "black", 8, "www")
print(sneakers1.hello())
sneakers1.set_size(0)
print(sneakers1.get_size())
sneakers1.set_wide('ww')
print(sneakers1.get_wide())
print(sneakers1.__dict__)
print(sandals1.__dict__)

