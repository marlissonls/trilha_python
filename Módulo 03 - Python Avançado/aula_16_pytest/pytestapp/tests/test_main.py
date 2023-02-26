from pytestapp.main import Advice
# import pytest

def test_init():
    advice = Advice()
    assert isinstance(advice, Advice)

def test_write_advice():
    advice = Advice()
    assert advice.write_advice() == "the advice was written to the file succesfully!"

#@pytest.mark.skip
def test_write_advice_exception():
    advice = Advice()
    assert advice.write_advice() == "Something went wrong!"

def test_show_old_advices():
    assert type(Advice.show_old_advices()) == list