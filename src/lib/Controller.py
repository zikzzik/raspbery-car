class Controller:

    def __init__(self, host, port, socket, car_name=None):
        self.host = host
        self.port = port
        self.socket = socket
        self.car_name = car_name

    def __hash__(self):
        return hash(self.host)

    def key(self):
        return self.host
