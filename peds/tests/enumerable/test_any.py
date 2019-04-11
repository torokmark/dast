import re

from unittest import TestCase
from expects import expect, equal, raise_error 

import peds

class TestAny(TestCase):
    def setUp(self):
        self.e = peds.Enumerable([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_any_if_regex_with_no_matching(self):
        e = peds.Enumerable(['apple', 'hola', 'appletree', 'applejuice', 'juice'])
        pattern = re.compile('le*')
        result = e.any(pattern)
        expect(result).to(equal(False))

    def test_any_if_regex_with_any_matching(self):
        e = peds.Enumerable(['apple', 'applehola', 'appletree', 'applejuice'])
        pattern = re.compile('apple*')
        result = e.any(pattern)
        expect(result).to(equal(True))

    def test_any_if_lambda_with_no_matching(self):
        predicate = lambda x: x % 11 == 0
        result = self.e.any(predicate)
        expect(result).to(equal(False))

    def test_any_if_lambda_with_any_matching(self):
        predicate = lambda x: x > 0 
        result = self.e.any(predicate)
        expect(result).to(equal(True))

    def test_any_if_lambda_with_any_matching(self):
        predicate = 'predicate'
        expect(lambda: self.e.any(predicate)).to(raise_error(TypeError))

