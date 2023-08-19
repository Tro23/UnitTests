class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def set_width(self,width):
        self.width = width

    def set_height(self,height):
        self.height = height

width, height = input("Enter Width and Height:\n").split()
print('width:', width)
print('height',height)

x = Rectangle(int(width),int(height))
print('Area is %d' % x.get_area())      