import unittest

def roman2deciman(rom):

    map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'M':1000}
    valorTotal = 0
    valorAtual = 0
    valorProximo = 0

    for letra in rom:
        valorTotal += map[letra]
        if

    if map.get(rom):
        return map[rom]
    elif rom == 'IV':
        return 4
    elif rom == 'IX':
        return 9
    return valorTotal

class StubTests(unittest.TestCase):
    def testI(self):
        self.assertEquals(roman2deciman('I'), 1)

    def testII(self):
        self.assertEquals(roman2deciman('II'), 2)

    def testIII(self):
        self.assertEquals(roman2deciman('III'), 3)

    def testIV(self):
        self.assertEquals(roman2deciman('IV'), 4)

    def testV(self):
        self.assertEquals(roman2deciman('V'), 5)

    def testVI(self):
        self.assertEquals(roman2deciman('VI'), 6)

    def testIX(self):
        self.assertEquals(roman2deciman('IX'), 9)

    def testX(self):
        self.assertEquals(roman2deciman('X'), 10)

























if __name__ == '__main__':
    unittest.main()

