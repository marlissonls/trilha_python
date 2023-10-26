class CustomExceptionA(Exception):
    pass

class CustomExceptionB(CustomExceptionA):
    pass

class CustomExceptionC(CustomExceptionB):
    pass

for cls in [CustomExceptionA, CustomExceptionB, CustomExceptionC]:
    try:
        raise cls()
    except CustomExceptionC:
        print('Exceção customizada C')
    except CustomExceptionB:
        print('Exceção customizada B')
    except CustomExceptionA:
        print('Exceção customizada A')
