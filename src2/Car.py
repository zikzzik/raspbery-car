class Car:

    def __init__(self, name, host, port, socket, used=False):
        self.name = name
        self.used = used

    def __hash__(self):
        return hash(self.name)

    def key(self):
        return self.name