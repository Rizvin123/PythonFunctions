"""Prints something"""
print("Hey this is test commit file + Now added something")

def adder(a, b):
    """Takes two integers and adds them together"""
    return a + b

def sub(a, b):
    """Takes two integers and substract them"""
    return a-b

def mult(a, b):
    """Takes two integers and multiplies them"""
    return a*b

def div(a, b):
    """Takes two integers and returns their quotient"""
    return a/b

RESULT1 = adder(5,8)
RESULT2 = sub(5,8)
RESULT3 = mult(5,8)
RESULT4 = div(5,8)

"""Prints the result"""
print(RESULT1)
print(RESULT2)
print(RESULT3)
