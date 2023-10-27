import unittest
from isTriangle import Triangle
# import sys
# sys.path.append("..")
# from src.Triangle import Triangle

class TriangleTest(unittest.TestCase):

    def testEquilateral(self):
        actual = Triangle.classify(5, 5, 5)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

    def testIsosceles1(self):
        actual = Triangle.classify(5, 5, 9)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def testIsosceles2(self):
        actual = Triangle.classify(4, 7, 4)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def testIsosceles3(self):
        actual = Triangle.classify(11, 6, 6)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def testScalene(self):
        actual = Triangle.classify(3, 4, 5)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)

    def testInvalidIsosceles1(self):
        actual = Triangle.classify(10, 5, 5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
    def testInvalidIsosceles2(self):
        actual = Triangle.classify(4, 8, 4)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
    def testInvalidIsosceles3(self):
        actual = Triangle.classify(6, 6, 12)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
    def testInvalidTriangle1(self):
        actual = Triangle.classify(11, 5, 4)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
    def testInvalidTriangle2(self):
        actual = Triangle.classify(9, 5, 4)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    
    def testInvalidTriangle3(self):
        actual = Triangle.classify(5, 9, 4)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
    def testInvalidTriangle4(self):
        actual = Triangle.classify(5, 4, 9)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
    def testInvalidIsoscelesZero1(self):
        actual = Triangle.classify(6,6,0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    
    def testInvalidIsoscelesZero2(self):
        actual = Triangle.classify(7,0,7)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    
    def testInvalidIsoscelesZero3(self):
        actual = Triangle.classify(0,3,3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        


if __name__ == '__main__':
    unittest.main()
