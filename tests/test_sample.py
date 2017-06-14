from services.sample_service import adding
from myexceptions import NumberFormatError
import pytest

def test_addition_works():
    assert adding(2,2) == 4

def test_only_numbers_as_args():
    with pytest.raises(NumberFormatError, message='Expecting a NumberFormatError exception'):
        adding("2","2")