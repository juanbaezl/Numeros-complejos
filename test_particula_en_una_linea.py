import unittest
from particula_en_una_linea import *
class TestStringMethods(unittest.TestCase):

    def test_probabilidad(self):
        v=[(2,1),(-1,2),(0,1),(1,0),(3,-1),(2,0),(0,-2),(-2,1),(1,-3),(0,-1)]
        f = 7
        self.assertEqual (probabilidad (v,f) , 10.87)


    def test_transitar(self):
        v=[(2,1),(-1,2),(0,1),(1,0),(3,-1),(2,0),(0,-2),(-2,1),(1,-3),(0,-1)]
        d=[(-1,-4),(2,-3),(-7,6),(-1,1),(-5,-3),(5,0),(5,8),(4,-4),(8,-7),(2,-7)]
        self.assertEqual (transitar (v,d) , [-0.02, -0.13])

if __name__ == '__main__':
    unittest.main()
