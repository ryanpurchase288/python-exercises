def upper_decorator(func):
    def func_wrapper(string1):
        return string1.upper()
    return func_wrapper

@upper_decorator
def hello(string1):
    return string1

print(hello('hello world'))