# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# Create function
def say_hello(name='Sam'):
    print(f'hello {name}')


# Return values
def get_sum(a, b):
    return a + b


print(get_sum(2, 2))


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

# lambda_get_sum = lambda a, b: a + b 
lambda_get_sum = lambda a, b: a + b 

print(lambda_get_sum(4,7))


