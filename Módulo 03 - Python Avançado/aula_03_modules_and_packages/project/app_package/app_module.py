"""
    The following 6 to 8 code lines are necessary to resolve the error:
        ModuleNotFoundError: No module named 'tests_package'. 
    So the real code beggins on line 10.
"""
from os.path import dirname, realpath
from sys import path
path.append(dirname(dirname(realpath(__file__))))

""" Importing from other packages """
# importing all modules defined in /tests_package/__init__.py from tests_package
from tests_package import *

# assigning the messages obtained from the modules imported from test_package to new variables
test_app_module_msg = test_app_module.message
test_some_module_msg = test_some_module.message

""" Importing from other packages """
""" # another way to do the earlier steps...
from tests_package.test_app_module import message as test_app_module_msg
from tests_package.test_some_module import message as test_some_module_msg """

""" Importing from the same package """
# importing a variable from a module in the same package
from some_module import message as some_module_msg

""" This was created here """
app_module_msg = "Hi! I'm the main module, my name is 'app_module.py' and 'app_package' is my home."

def main():
    all_messages = [
        app_module_msg,
        some_module_msg,
        test_app_module_msg,
        test_some_module_msg
    ]

    for message in all_messages:
        print(message, end="\n\n")

if __name__ == '__main__':
    main()

"""
    OUTPUT

Hi! I'm the main module, my name is 'app_module.py' and 'app_package' is my home.

Hello! I'm some module, my name is 'some_module.py' and 'app_package' is my home.

Hi! I'm a test for the main module, my name is 'test_app_module.py' and 'tests_package' is my home.

Hello! I'm a test for some module, my name is 'test_some_module.py' and 'tests_package' is my home.
"""