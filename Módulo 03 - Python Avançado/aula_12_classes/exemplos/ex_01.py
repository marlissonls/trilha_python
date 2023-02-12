def	cria_conta(numero,	titular, saldo,	limite):
    conta =	{
        "numero": numero, 
        "titular": titular, 
        "saldo": saldo, 
        "limite": limite
    }
    return conta

def	deposita(conta,	valor):
    conta['saldo'] += valor

def	saca(conta,	valor):
	conta['saldo'] -= valor

def	extrato(conta):
	print("numero: {} \nsaldo: {}".format(conta['numero'], conta['saldo']))

""" conta = cria_conta('123-7', 'João', 500.0, 1000.0)
deposita(conta, 50.0)
extrato(conta)
#numero: '123-7'
#saldo:	550.0
saca(conta,	20.0)
extrato(conta)
#numero: '123-7 """