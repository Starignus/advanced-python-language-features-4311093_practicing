# Example file for Advanced Python: Language Features by Joe Marini
# Demonstrate the use of keyword-only arguments


# use keyword-only arguments to help ensure code clarity
def MyFunction(arg1, arg2=False, *, supress_exc=False):
    pass


# try to call the function without the keyword
# MyFunction(1,2,True) # we get an error  of: TypeError: MyFunction() takes 2 positional arguments but 3 were given
# correct way to call the function is supplying the keyword
MyFunction(1,2,supress_exc=True)