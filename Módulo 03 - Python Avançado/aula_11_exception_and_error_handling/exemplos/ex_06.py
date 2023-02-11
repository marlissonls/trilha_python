def bool_return():
    try:
        return True
    finally:
        return False

if bool_return() == True:
    print('True')
else:
    print('False')