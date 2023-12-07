"""Python serial number generator."""

class SerialGenerator:

    def __init__(self, start =100):
        self.start = start
        self.current = start

    def generate(self):
        serial = self.current
        self.current += 1 
        return serial

    def reset(self):
        self.current = self.start

serial = SerialGenerator(start = 100)


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
print(serial.generate())
print(serial.generate())
print(serial.generate())

serial.reset()

print(serial.generate())