import unittest

with open("C:\\Codes\\Unit_Test\\Rectangle.py") as f:
    exec(f.read())

class TestGetAreaRectangle(unittest.TestCase):
    def runTest(self):
        rectangle = Rectangle(2,3)
        self.assertEqual(rectangle.get_area(),6,"incorrect area")


unittest.main()