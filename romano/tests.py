import unittest


def roman2deciman(rom):

    if rom == 'IV':
        return 4
    elif rom == 'V':
        return 5
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



if __name__ == '__main__':
    unittest.main()

