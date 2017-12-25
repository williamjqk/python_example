# %%
def double_inputs():
    while True:
        x = yield
        yield x * 2

gen = double_inputs()
# gen.next() # cannot work in Python 3.6
gen.__next__() #run up to the first yield
gen.send(10) #goes into 'x' variable

# %%
def double_inputs():
    while True:
        x = yield
        yield x * 2

gen = double_inputs()
gen.send(None)
gen.send(10) #goes into 'x' variable


# %%
def double_inputs():
    x = 0
    while True:
        # x = yield x
        x = yield x * 2
        # yield x

gen = double_inputs()
gen.send(None)
gen.send(10) #goes into 'x' variable


# %%
def double_inputs():
    x = 12
    while True:
        yield x * 2

gen = double_inputs()
gen.send(None) #run up to the first yield
gen.send(10) #goes into 'x' variable

# %%
def loop_gen():
    for i in range(5):
        yield i
[x for x in loop_gen()]

# %%
def inner_generator():
    i = 0
    while True:
        i = yield i
        if i > 10:
            raise StopIteration

def outer_generator():
    print("do something before yield")
    from_inner = 0
    from_outer = 1
    g = inner_generator()
    g.send(None)
    while 1:
        try:
            from_inner = g.send(from_outer)
            from_outer = yield from_inner * 2
        except StopIteration:
            break

def main():
    g = outer_generator()
    g.send(None)
    i = 0
    while 1:
        try:
            i = g.send(i + 1)
            print(i)
        except StopIteration:
            break


if __name__ == '__main__':
    main()

# %%
def inner_generator():
    i = 0
    while True:
        i = yield i
        if i > 10:
            raise StopIteration


def outer_generator():
    print("do something before coroutine start")
    yield from inner_generator()


def main():
    g = outer_generator()
    g.send(None)
    i = 0
    while 1:
        try:
            i = g.send(i + 1)
            print(i)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
