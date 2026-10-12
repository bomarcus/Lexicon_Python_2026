# Lab-9_G-2

# Create Computer with brand and a CPU object. Use composition, not inheritance

class CPU:
    def __init__(self, model):
        self.model = model


class Computer:
    def __init__(self, cpu, brand):
        self.cpu = cpu
        self.brand = brand
