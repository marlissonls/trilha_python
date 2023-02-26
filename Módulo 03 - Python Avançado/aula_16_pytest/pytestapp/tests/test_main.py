from pytestapp.main import Advice
# import pytest

class TestAdvice:
    def test_init(self):
        advice = Advice()
        assert isinstance(advice, Advice)

    def test_write_advice(self):
        advice = Advice()
        assert advice.write_advice() == "the advice was written to the file succesfully!"

    #@pytest.mark.skip
    def test_write_advice_exception(self):
        advice = Advice()
        assert advice.write_advice() == "Something went wrong!"

    def test_show_old_advices(self):
        assert type(Advice.show_old_advices()) == list