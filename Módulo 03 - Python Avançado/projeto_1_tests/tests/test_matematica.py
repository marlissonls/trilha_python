import os, sys
  #add projeto      # projeto       # tests          # tests/thisfile.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from app.matematica import Matematica

def test_somar():
    assert Matematica.somar(1, 1) == 2