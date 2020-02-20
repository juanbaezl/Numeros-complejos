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
            self.assertEqual (mod (v[0],v[1]) , 3.16)

    def test_fase (self) :
        v = (1,1)
        self.assertEqual (fase (v[0],v[1]) , (45))

    def test_polar (self):
        v = (1,1)
        self.assertEqual (pol (v[0],v[1]) , (1.41 , 45))

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

    def test_summat (self):
        d=[(1,2),(3,2)],[(3,3),(4,2)]
        v=[(1,2),(3,2)],[(2,2),(5,2)]
        self.assertEqual (addmat (d,v),[[(2, 4), (6, 4)], [(5, 5), (9, 4)]])

    def test_invmat (self):
         d=[(1,2),(3,2)],[(3,3),(4,2)]
         self.assertEqual (invmat(d),[[(-1, -2), (-3, -2)], [(-3, -3), (-4, -2)]])

    def test_escalmat (self):
         d=[(1,2),(3,2)],[(3,3),(4,2)]
         f=4
         self.assertEqual (mult_escal (d,f),[[(4, 8), (12, 8)], [(12, 12), (16, 8)]] )

    def test_transpuesta (self):
         d=[(1,2),(3,2)],[(3,3),(4,2)]
         self.assertEqual (transpuesta  (d),[[(1, 2), (3, 3)], [(3, 2), (4, 2)]])

    def test_conjugmat (self):
        d=[(1,2),(3,2)],[(3,3),(4,2)]
        self.assertEqual (conjugmat (d),[[(1, -2), (3, -2)], [(3, -3), (4, -2)]])

    def test_adjunta (self):
        d=[(1,2),(3,2)],[(3,3),(4,2)]
        self.assertEqual (adjunta(d),[[(1, -2), (3, -3)], [(3, -2), (4, -2)]])

    def test_multimat (self):
        d=[(1,2),(3,2)],[(3,3),(4,2)]
        v=[(1,2),(3,2)],[(2,2),(5,2)]
        self.assertEqual (multimat (v,d), [[(0, 19), (7, 22)], [(7, 27), (18, 28)]])

    def test_accion (self):
        d=[(1,2),(3,2)],[(3,3),(4,2)]
        v=[(1,2),(3,2)]
        self.assertEqual (accion (d,v), [(2, 16), (5, 23)])

    def test_interno (self):
        d=[(1,2),(3,2),(2,2),(5,2)]
        v=[(1,2),(3,2),(2,2),(5,2)]
        self.assertEqual (interno (v,d),(55, 0))

    def test_norma (self):
        v=[(1,2),(3,2),(2,2),(5,2)]
        self.assertEqual (norma_vect (v), 7.42)

    def test_distancia (self):
        d=[(1,2),(3,2),(3,3),(4,2)]
        v=[(1,2),(3,2),(2,2),(5,2)]
        self.assertEqual (dist(v,d),1.73)

    def test_unitaria (self):
        d=[(1,0),(0,0)],[(0,0),(1,0)]
        self.assertEqual (unitaria(d), True)

    def test_hermitiana (self):
        d=[[(1,0),(0,0)],[(0,0),(1,0)]]
        self.assertEqual (unitaria(d), True)

    def test_tensor (self):
        d=[(1,2),(3,2)],[(3,3),(4,2)]
        v=[(1,1),(1,1)],[(1,1),(1,1)]
        self.assertEqual (tensor(v,d), [[(-1, 3), (1, 5), (-1, 3), (1, 5)], [(0, 6), (2, 6), (0, 6), (2, 6)], [(-1, 3), (1, 5), (-1, 3), (1, 5)], [(0, 6), (2, 6), (0, 6), (2, 6)]])
if __name__ == '__main__':
    unittest.main()
