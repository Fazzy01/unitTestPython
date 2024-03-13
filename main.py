
# function that do addition
def addNumber(a,b):
    # if type(a) == str :
    #     return "This is not a number"
    if isinstance(a,str) | isinstance(b,str):
        return "one of your inputs is not a number"
    else:
        return a + b    

addition = addNumber(4,6)
print(addition)