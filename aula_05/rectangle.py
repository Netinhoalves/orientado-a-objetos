class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    
    def set_dimensions(self, w, h):
        self.width = w
        self.height = h
    
    def get_area(self):
        return self.width * self.height
    
#como usar:
retangulo = Rectangle()
retangulo.set_dimensions(10, 5)
print(retangulo.get_area())