class FakeDatabase:
    def __init__(self):
        self.connected = False

    def connect(self):
        self.connected = True
        return True

    def is_connected(self):
        return self.connected
