
import re
from unittest import TestCase
from expects import expect, equal, raise_error, be_true, be_false 

from peds import List 

class TestReject(TestCase):

    def test_reject_if_lambda_is_none(self):
        e = List([None, 5, 0, [], 3, 5, 2, '', 4])
        expect(e.reject()).to(equal([None, 0, [], '']))

    def test_reject_if_list_is_empty(self):
        e = List([])
        expect(e.reject(lambda x: x == 1)).to(equal([]))
  
    def test_reject_if_lambda_is_valid_greater_than(self):
        e = List([5, 3, 5, 2, 4])
        expect(e.reject(lambda x: x > 3)).to(equal([3, 2]))

    def test_reject_if_lambda_is_valid_len(self):
        e = List(['apple', 'caterpillar', 'bear', 'dog', 'plum'])
        expect(e.reject(lambda x: len(x) > 5)).to(equal(['apple', 'bear', 'dog', 'plum']))
    
    def test_reject_if_lambda_is_different(self):
        e = List(['apple', 'caterpillar', 'bear', 'dog', 'plum'])
        expect(lambda: e.reject('...')).to(raise_error(TypeError)) 
