class Card:
    def __init__(self, name):
        self.name = name

    def apply(self, consumer, opponent):
        raise NotImplementedError("Implement apply for {0}".format(type(self)))

    def __repr__(self):
        return self.name