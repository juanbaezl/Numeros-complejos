import unittest
from libreria import *
class TestStringMethods(unittest.TestCase):

    def test_suma(self):
        v = (3,1)
        d = (4,5)
        self.assertEqual (suma (v,d) , (7,6))


    def test_resta(self):
              v = (3,1)
              d = (4,5)
              self.assertEqual (resta (v,d) , (-1,-4))

    def test_multiplicación(self):
            v = (3,1)
            d = (4,5)
            self.assertEqual (mult (v,d) , (7,19))

    def test_división(self):
            v = (1,3)
            d = (1,1)
            self.assertEqual (div (v,d) , (2,1))

    def test_conjugada(self):
            v = (3,1)
            self.assertEqual (conjug (v) , (3,-1))

    def test_modulo(self):
            v = (3,1)
            self.assertEqual (mod (v[0],v[1]) , (10**(1/2)))

    def test_fase (self) :
        v = (1,1)
        self.assertEqual (fase (v[0],v[1]) , (45))

    def test_polar (self):
        v = (1,1)
        self.assertEqual (pol (v[0],v[1]) , ((2**(1/2)) , 45))

    def test_addvect (self):
        d=[(1,2),(1,2),(1,2),(1,2)]
        v=[(1,2),(1,2),(1,2),[1,2]]
        self.assertEqual (addvect (v,d), [(2, 4), (2, 4), (2, 4), (2, 4)])

    def test_inversa (self):
        v = [(1,2),(1,2)]
        self.assertEqual (inverse (v) , [(-1,-2),(-1,-2)])

    def test_escalvect (self):
        v=[(1,2),(1,2),(1,2),[1,2]]
        f=4
        self.assertEqual (escal (v,f),[(4, 8), (4, 8), (4, 8), (4, 8)])


if __name__ == '__main__':
        unittest.main()

