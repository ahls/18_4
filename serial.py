"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """start: default number that starts off. when Reset is called, the current number will be set to start"""
        self.start = start
        self.num = start
    

    def generate(self):
        """Returns the current number"""
        self.num += 1
        return self.num - 1
    

    def reset(self):
        """sets the current number back to the starting number"""
        self.num = self.start
    
    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.num}>"


