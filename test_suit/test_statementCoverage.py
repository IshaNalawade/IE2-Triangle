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
        actual = Triangle.classify(9, 5, 5)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def testScalene(self):
        actual = Triangle.classify(3, 4, 5)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)
    
    def testInvalid(self):
        actual = Triangle.classify(-1, 9, 4)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    
    def testInvalidIsosceles(self):
        actual = Triangle.classify(11, 5, 5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def testInvalidScalene(self):
        actual = Triangle.classify(3, 4, 1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
    def testIsosceles2(self):
        actual = Triangle.classify(4, 4, 7)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)
    
    def testIsosceles3(self):
        actual = Triangle.classify(3, 4, 3)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
