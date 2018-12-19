import unittest
from machine import Machine

class TestAddrInsn(unittest.TestCase):
    def setUp(self):
        self.m = Machine([1, 2, 10, 20])

    def test_addr_1(self):
        self.m.execute(['addr', 0, 1, 2])
        self.assertEqual(self.m.registers, [1, 2, 3, 20])

    def test_addr_2(self):
        self.m.execute(['addr', 1, 2, 3])
        self.assertEqual(self.m.registers, [1, 2, 10, 12])

    def test_addr_3(self):
        self.m.execute(['addr', 2, 3, 0])
        self.assertEqual(self.m.registers, [30, 2, 10, 20])

    def test_addr_4(self):
        self.m.execute(['addr', 3, 0, 1])
        self.assertEqual(self.m.registers, [1, 21, 10, 20])

    def test_addr_5(self):
        self.m.execute(['addr', 1, 1, 2])
        self.assertEqual(self.m.registers, [1, 2, 4, 20])

class TestAddiInsn(unittest.TestCase):
    def setUp(self):
        self.m = Machine([1, 5, 10, 19])

    def test_addi_1(self):
        self.m.execute(['addi', 0, 10, 0])
        self.assertEqual(self.m.registers, [11, 5, 10, 19])

    def test_addi_2(self):
        self.m.execute(['addi', 0, 10, 1])
        self.assertEqual(self.m.registers, [1, 11, 10, 19])

class TestMulrInsn(unittest.TestCase):
    def setUp(self):
        self.m = Machine([1, 5, 20, 30])

    def test_1(self):
        self.m.execute(['mulr', 0, 1, 2])
        self.assertEqual(self.m.registers, [1, 5, 5, 30])

    def test_2(self):
        self.m.execute(['mulr', 1, 2, 1])
        self.assertEqual(self.m.registers, [1, 100, 20, 30])

    def test_3(self):
        self.m.execute(['muli', 1, 10, 2])
        self.assertEqual(self.m.registers, [1, 5, 50, 30])

    def test_4(self):
        self.m.execute(['banr', 0, 1, 2])
        self.assertEqual(self.m.registers, [1, 5, 1, 30])

    def test_5(self):
        self.m.execute(['bani', 1, 10, 2])
        self.assertEqual(self.m.registers, [1, 5, 0, 30])

    def test_5(self):
        self.m.execute(['borr', 1, 2, 3])
        self.assertEqual(self.m.registers, [1, 5, 20, 21])

    def test_6(self):
        self.m.execute(['bori', 1, 10, 3])
        self.assertEqual(self.m.registers, [1, 5, 20, 15])

    def test_7(self):
        self.m.execute(['setr', 3, 10, 0])
        self.assertEqual(self.m.registers, [30, 5, 20, 30])

    def test_7(self):
        self.m.execute(['seti', 30, 10, 1])
        self.assertEqual(self.m.registers, [1, 30, 20, 30])

    # [1, 5, 20, 30]
    def test_7(self):
        self.m.execute(['gtir', 0, 1, 2])
        self.assertEqual(self.m.registers, [1, 5, 0, 30])

    # [1, 5, 20, 30]
    def test_7(self):
        self.m.execute(['gtir', 6, 1, 2])
        self.assertEqual(self.m.registers, [1, 5, 1, 30])

    # [1, 5, 20, 30]
    def test_8(self):
        self.m.execute(['gtrr', 1, 2, 3])
        self.assertEqual(self.m.registers, [1, 5, 20, 0])

    # [1, 5, 20, 30]
    def test_9(self):
        self.m.execute(['gtrr', 2, 1, 3])
        self.assertEqual(self.m.registers, [1, 5, 20, 1])

    # [1, 5, 20, 30]
    def test_10(self):
        self.m.execute(['eqir', 5, 1, 3])
        self.assertEqual(self.m.registers, [1, 5, 20, 1])

    # [1, 5, 20, 30]
    def test_11(self):
        self.m.execute(['eqir', 6, 1, 3])
        self.assertEqual(self.m.registers, [1, 5, 20, 0])

    # [1, 5, 20, 30]
    def test_12(self):
        self.m.execute(['eqri', 1, 5, 3])
        self.assertEqual(self.m.registers, [1, 5, 20, 1])

    # [1, 5, 20, 30]
    def test_13(self):
        self.m.execute(['eqri', 1, 6, 3])
        self.assertEqual(self.m.registers, [1, 5, 20, 0])

    # [1, 5, 20, 30]
    def test_14(self):
        self.m.execute(['eqrr', 1, 2, 3])
        self.assertEqual(self.m.registers, [1, 5, 20, 0])

    # [1, 5, 20, 30]
    def test_14(self):
        self.m.execute(['setr', 1, 2, 3])
        self.m.execute(['eqrr', 1, 3, 2])
        self.assertEqual(self.m.registers, [1, 5, 1, 5])

if __name__ == '__main__':
    unittest.main()
