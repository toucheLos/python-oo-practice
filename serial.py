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
    "Base serial generator"

    def __init__(self, start):
        "Create the base serial number"
        self.start = start
        self.current = start
    
    def __repr__(self):
        return f"<SerialGenerator start = {self.start} current = {self.current - 1}>"
    
    def generate(self):
        "Add one to the current value of the serial and return value"
        self.current += 1
        return self.current - 1
        
    def reset(self):
        "Reset the serial number to original class value"
        self.current = self.start