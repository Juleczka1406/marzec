#! /usr/bin/python

import unittest

import TDD

import random

import re

class TestStringMethods(unittest.TestCase):

    def test_f1_1(self):
        k=TDD.f1(0)
        self.assertEqual(k, 0)

    def test_f1_2(self):
        k1=TDD.f1(1)
        self.assertEqual(k1, 1)

    def test_f1_3(self):
        k2=TDD.f1(2)
        self.assertEqual(k2, 4)

    def test_f1_4(self):
        k3=TDD.f1(2, 1)
        self.assertEqual(k3, 5)

    def test_f1_5(self):
        k4=TDD.f1(2, 3)
        self.assertEqual(k4, 7)

    def test_f2_1(self):
        k5=TDD.f2("ala")
        self.assertEqual(k5, "a")

    def test_f2_2(self):
        k6=TDD.f2([1,2,3])
        self.assertEqual(k6, 1)

    def test_f2_3(self):
        k7=TDD.f2([])
        self.assertEqual(k7, "BUUM")

    def test_f3_1(self):
        k8=TDD.f3(1)
        self.assertEqual(k8, "jeden")

    def test_f3_2(self):
        k9=TDD.f3(2)
        self.assertEqual(k9, "dwa")

    def test_f3_3(self):
        k10=TDD.f3(3)
        self.assertEqual(k10, "trzy")

    def test_f3_4(self):
        k11=TDD.f3(random.choice(range(4, 1000)))
        self.assertEqual(k11, 'other')

    def test_f4_1(self):
        k12=TDD.f4("ala")
        self.assertEqual(k12, "ala ma kota")

    def test_f4_2(self):
        k13=TDD.f4("kot")
        self.assertEqual(k13, "kot ma kota")

    def test_f4_3(self):
        k14=TDD.f4("kot", "psa")
        self.assertEqual(k14, "kot ma kota i psa")

    def test_f4_4(self):
        k15=TDD.f4("kot", "mysz")
        self.assertEqual(k15, "kot ma kota i mysz")

    def test_f5_1(self):
        k16=TDD.f5(0)
        self.assertEqual(k16, [])

    def test_f5_2(self):
        k17=TDD.f5(1)
        self.assertEqual(k17, [0])

    def test_f5_3(self):
        k18=TDD.f5(2)
        self.assertEqual(k18, list(range(2)))

    def test_f5_4(self):
        k19=TDD.f5(7)
        self.assertEqual(k19, list(range(7)))

    def test_f5_5(self):
        k20=TDD.f5(7,2)
        self.assertEqual(k20, [0, 2, 4, 6])

    def test_f5_6(self):
        k21=TDD.f5(17, 2)
        self.assertEqual(k21, [0, 2, 4, 6, 8, 10, 12, 14, 16])

    def test_f6_1(self):
        k22=TDD.f6(1, "*")
        self.assertEqual(k22, "*")

    def test_f6_2(self):
        k23=TDD.f6(7, "*")
        self.assertEqual(k23, "*******")

    def test_f7_1(self):
        k24=TDD.f7("ala")
        self.assertEqual(k24, "slowo")

    def test_f7_2(self):
        k25=TDD.f7("1")
        self.assertEqual(k25, "cyfra")

    def test_f7_3(self):
        k26=TDD.f7("11111")
        self.assertEqual(k26, "liczba")

    def test_f7_4(self):
        k27=TDD.f7("-11111")
        self.assertEqual(k27, "liczba_ze_znakiem")

    def test_f7_5(self):
        k28=TDD.f7("Ala ma kota.")
        self.assertEqual(k28, "zdanie")

    def test_f7_5(self):
        k29=TDD.f7("<taaag>")
        self.assertEqual(k29, "tag poczatkowy")

    def test_f7_5(self):
        k30=TDD.f7("</taaag>")
        self.assertEqual(k30, "tag koncowy")

    def test_test(self):
        self.assertTrue(True)

    if __name__ == '__main__':
        unittest.main()
