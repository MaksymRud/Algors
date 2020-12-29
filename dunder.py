class Circle:
    #__slots__ = ['diametr']

    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self.diameter / 2.0
    
    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2.0

    @property
    def diameter(self):
        return self.diameter 

    @diameter.setter
    def diameter(self, diameter):
        self.diameter = diameter
    
    

c = Circle(4)
c.radius = 5
print(c.radius)
print(c.diameter)

class Base:
    def __init__(self, arg):
        self.arg = arg

    def __func(self):
        return self.arg
    
    def get_arg(self):
        return self.__func()

class Derive(Base):
    def __init__(self, arg):
        super().__init__(arg)

    def _func(self):
        return self.arg
    
b = Base(3)
print(b.get_arg())
d = Derive(4)
print(d._func())
