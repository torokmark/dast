from unittest import TestCase
from expects import expect, equal, raise_error 

import peds

class TestIter(TestCase):
    def setUp(self):
        self.e = peds.Enumerable([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_iter_if_empty(self):
        e = peds.Enumerable([])
        it = iter(e)
        expect(lambda: next(it)).to(raise_error(StopIteration))

    def test_iter_if_non_empty(self):
        it = iter(self.e)
        expect(next(it)).to(equal(1))
        expect(next(it)).to(equal(2))
        expect(next(it)).to(equal(3))
        expect(next(it)).to(equal(4))
        expect(next(it)).to(equal(5))


