# Lab-9_G-5

# In comments, explain why "Computer HAS-A CPU" makes more sense than "Computer IS-A CPU"

class CPU:
    def __init__(self, model):
        self.model = model


class Computer:
    def __init__(self, cpu, brand):
        self.cpu = cpu
        self.brand = brand


cpu = CPU("Intel")
computer = Computer(cpu, "Dell")

print(computer.brand, computer.cpu.model)


# Dog IS-A Animal → inheritance.
# Computer HAS-A CPU → composition.
