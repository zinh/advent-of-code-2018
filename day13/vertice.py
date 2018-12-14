class Vertice:
    def __init__(self, label):
        self.label = label
        self.__left = None
        self.__right = None
        self.__top = None
        self.__bottom = None

    @property
    def left(self):
        return self.__left

    @property
    def right(self):
        return self.__right

    @property
    def top(self):
        return self.__top

    @property
    def bottom(self):
        return self.__bottom

    @left.setter
    def left(self, v):
        self.__left = v

    @right.setter
    def right(self, v):
        self.__right = v

    @top.setter
    def top(self, v):
        self.__top = v

    @bottom.setter
    def bottom(self, v):
        self.__bottom = v
