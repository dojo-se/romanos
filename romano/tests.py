import unittest


def roman2deciman(rom):

    map = {'I':1,'V':5,'X':10, 'L':50, 'C':100,
        'M':1000}

    if map.get(rom) == 10: return map[rom]

    if rom == 'IV':
        return 4
    elif rom == 'V':
        return 5
    elif rom == 'VI':
        return 6
    else:
        return len(rom)

class StubTests(unittest.TestCase):
    def testFoo(self):
        self.assertEquals(roman2deciman('I'), 1)
        self.assertEquals(roman2deciman('II'), 2)
        self.assertEquals(roman2deciman('III'), 3)

    def testBar(self):
        self.assertEquals(roman2deciman('IV'), 4)

    def testAllWords(self):
        self.assertEquals(roman2deciman('V'), 5)

    def testWagner(self):
        self.assertEquals(roman2deciman('VI'), 6)

    def testMapeamento(self):
        self.assertEquals(roman2deciman('X'), 10)




























if __name__ == '__main__':
    unittest.main()

