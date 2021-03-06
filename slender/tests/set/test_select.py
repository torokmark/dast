from unittest import TestCase
from expects import expect, equal, raise_error, be_false, be_true 

from slender import Set 

class TestSelect(TestCase):

    def test_select_if_self_is_empty(self):
        e = Set[int]()
        expect(e.select(lambda x: x % 2 == 0)).to(equal(Set[int]()))

    def test_select_if_no_match(self):
        e = Set[int]({1, 2, 3, 4})
        expect(e.select(lambda x: x > 5)).to(equal(Set[int]()))

    def test_select_if_all_match(self):
        e = Set[int]({1, 2, 3, 4, 5})
        expect(e.select(lambda x: x >= 1)).to(equal(Set[int]({1, 2, 3, 4, 5})))

    def test_select_if_partial_match(self):
        e = Set[int]({1, 2, 3, 4})
        expect(e.select(lambda x: x % 2 == 0)).to(equal(Set[int]({2, 4})))

    def test_select_lambda_is_different(self):
        e = Set[int]({1, 2, 3})
        expect(lambda: e.select('...')).to(raise_error(TypeError))




