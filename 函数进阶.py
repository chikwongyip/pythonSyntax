def f(x):
    x = x + 1
   
    return(x)

def square(x):
    return x*x

def cube(x):
    return x*x*x

funcs = {
    'add_one': f,
    "square" : square,
    "cube"   : cube,
}
x = 9

print(funcs["add_one"](x) + funcs["square"](x) + funcs["cube"](x))