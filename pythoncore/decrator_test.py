# 关于多参数decorator, stackoverflow上的一个解释
# def decorator(argument):
#     def real_decorator(function):
#         def wrapper(*args, **kwargs):
#             funny_stuff()
#             something_with_argument(argument)
#             function(*args, **kwargs)
#             more_funny_stuff()
#         return wrapper
#     return real_decorator

def mask_test(f):
    def wrapper(*args, **kwargs):
        return '*'+str(f(*args,**kwargs))+'*'
    return wrapper

def outer_mask(in1):
    def wrapper(f):
        def wrapper_in(*args, **kwargs):
            return str(in1)+'*'+str(f(*args,**kwargs))+'*'
        return wrapper_in
    return wrapper

@mask_test
def haha(x,y):
    return x*y

@outer_mask('output: ')
def hehe(x,y):
    return x*y

print(haha(2.0,3.0))
print(hehe(2.0,3.0))

# %%
def hoho(x,y):
    return x*y
d1 = mask_test(hoho)
print(d1(2.0,3.0), hoho(2.0, 3.0))

# %% 多层decorator
def mask_layer2(f):
    def wrapper(*args, **kwargs):
        return '#'+str(f(*args, **kwargs))+'#'
    return wrapper

@mask_layer2
@mask_test
def hihi(x,y):
    return x*y

print(hihi(2.0,3.0))
