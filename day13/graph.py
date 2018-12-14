from cart import Cart
from vertice import Vertice

class Graph:
    def __init__(self):
        self.vertices = {}
        self.carts = []

    def connect(self, label1, label2, direction):
        v1 = self.vertices.setdefault(label1, Vertice(label1))
        v2 = self.vertices.setdefault(label2, Vertice(label2))
        if direction == '→':
            v1.right = v2
            v2.left = v1
        elif direction == '←':
            v1.left = v2
            v2.right = v1
        elif direction == '↑':
            v1.top = v2
            v2.bottom = v1
        elif direction == '↓':
            v1.bottom = v2
            v2.top = v1

    def add_cart(self, position, direction):
        v = self.vertices.setdefault(position, Vertice(position))
        cart = Cart(v, direction)
        self.carts.append(cart)

    def tick(self):
        for cart in self.carts:
            cart.run()
        labels = {}
        for cart in self.carts:
            label = cart.vertice.label
            if labels.get(label):
                return label
            labels[label] = True
        return None
