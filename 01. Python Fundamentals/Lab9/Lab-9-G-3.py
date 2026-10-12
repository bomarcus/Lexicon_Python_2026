# Lab-9_G-3

# Create a CPU object and pass it to a Computer object.

class CPU:
    def __init__(self, model):
        self.model = model


class Computer:
    def __init__(self, cpu, brand):
        self.cpu = cpu
        self.brand = brand


cpu = CPU("Intel")
computer = Computer(cpu, "Dell")
