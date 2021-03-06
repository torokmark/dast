from unittest import TestCase
from expects import expect, equal, raise_error, be_false, be_true 

from slender import Set 

class TestIssubset(TestCase):

    def test_issubset_self_is_subset_of_other_set(self):
        e = Set({2, 3})
        o = {1, 2, 3, 4}
        expect(e.issubset(o)).to(be_true)

    def test_issubset_self_is_not_subset_of_other_set(self):
        e = Set({1, 2, 3, 4})
        o = {0, 1, 2, 3}
        expect(e.issubset(o)).to(be_false)

    def test_issubset_self_is_subset_of_other_enhanced_set(self):
        e = Set({1, 2, 3, 4, 5})
        o = Set({1, 4, 2, 3, 5})
        expect(e.issubset(o)).to(be_true)

    def test_issubset_self_is_not_subset_of_other_enhanced_set(self):
        e = Set({1, 2, 3, 4})
        o = Set({0, 1, 2, 3})
        expect(e.issubset(o)).to(be_false)

    def test_issubset_other_is_different(self):
        e = Set({1, 2, 3})
        expect(lambda: e.issubset('...')).to(raise_error(TypeError))




