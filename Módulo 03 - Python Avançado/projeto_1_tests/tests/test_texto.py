import os, sys
  #add projeto      # projeto       # tests          # tests/thisfile.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from app.texto import Texto

def test_texto():
    assert Texto.texto('olá mundo') == 'olá mundo'