from pytestapp.main import Advice
# import pytest

class TestAdvice:
    def test_init(self):
        advice = Advice()
        assert isinstance(advice, Advice)

    def test_write_advice(self):
        advice = Advice()
        assert advice.write_advice() == "The advice was written to the file succesfully!"

    #@pytest.mark.skip
    def test_write_advice_exception(self):
        advice = Advice()
        assert advice.write_advice() == "Something went wrong! The advice wasn't written to the file."

    def test_show_old_advices(self):
        assert type(Advice.show_old_advices()) == list
    
    #@pytest.mark.skip
    def test_show_old_adviesce_exception(self):
        assert Advice.show_old_advices() == "Something went wrong! The file cannot be read."