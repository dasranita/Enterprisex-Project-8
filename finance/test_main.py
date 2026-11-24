from main import tax
from decimal import Decimal as D
def test_rounding():
    assert tax(D('0.05'),D('10'))==D('0.01')
def test_zero():
    assert tax(D('100'),D('0'))==D('0.00')
