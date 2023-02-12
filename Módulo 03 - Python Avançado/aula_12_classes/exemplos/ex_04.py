class Conta:
    def __init__(self, saldo):
        self._saldo = saldo

    def	get_saldo(self):
        return self._saldo
    
    def set_saldo(self, saldo):
        self._saldo = saldo


class Conta:
    def	__init__(self, saldo=0.0):
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo	
    			
    @saldo.setter
    def saldo(self, saldo):
        if(saldo < 0):
            print("saldo não pode ser negativo")
        else:
            self._saldo = saldo

@property
def foo(self):
	return self._foo

@foo.setter()

#é	equivalente	a:
def	foo(self):
	return self._foo
foo = property(foo)

#@foo.setter()
