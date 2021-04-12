'''
    Base component class

    Should not be accessed directly.
'''
class component():
    "Base component class."
    def __init__(self, *arg):
        self.name = ""
        if isinstance(arg[0], str):
            self.name  = arg[0]
            self.value = arg[1]
            self.node  = list(arg[2:])
        elif isinstance(arg[0], float):
            self.value = arg[0]
            self.node  = list(arg[1:])

    def getInfo(self):
        info = ""
        if self.name != "":
            info = self.name + " - "
        info += str(self.value) + " - "
        info += str(self.node)
        return info

'''
    Resistor component class

    resistor(name, value, t1, t2)
        name : component name or reference (optional) - type: string
        value: component value in ohms - type: float
        t1   : node where terminal 1 is connected - type: integer
        t2   : node where terminal 2 is connected - type: integer
    
    Examples:
        resistor(10.0e3, 7, 8)
        resistor("R1", 20.0, 9, 0)
'''
class resistor(component):
    "Resistor component class."
    kind = "resistor"
    
    def resistance(self):
        return self.value

    def conductance(self):
        return 1 / self.value

    def getInfo(self):
        return self.kind + " - " + super().getInfo()

'''
    Modeller main class
'''
class modeller:
    def __init__(self):
        self.components = []

    def add(self, components):
        for component in components:
            self.components.append(component)

    def run(self):
        for component in self.components:
            print(component.getInfo())

m = modeller()
r1 = resistor("R1", 10.0e3, 7, 8)
m.add([
    r1,
    resistor(20.0e3, 1, 2),
    resistor(30.0e3, 3, 4),
    resistor(40.0e3, 3, 5), 
    resistor(50.0e3, 5, 7)
    ])
m.run()
print(r1.kind)
print(r1.value)
print(r1.resistance())
print(r1.conductance())

m2 = modeller()
m2.add([
    resistor(70.0e3, 0, 7)
    ])
m2.run()
