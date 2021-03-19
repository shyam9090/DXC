import pytest #it is python unit testing module
from  program import fibonacci  # importing the function which need to be the tested
#positive scenario
'''If user enter any the positive number then it will return the below response'''
def test_program1():
    assert fibonacci(8) == [0,1,1,2,3,5,8,13] 
    
#negative scenario
'''If user enter negative number then it will return the below response'''
def test_program2():
    assert fibonacci(-3) == "can't calculate the fibonacci series"
    
'''
For running unit test script open the terminal in the file location and
then type pytest test_program.py
'''