def generator():
    yield 1
    yield 3
    yield 2
g=generator()
# return fn that can be iterated over ; generate only one object at a time when we ask for it
# memory efficient
"""value=next(g)
print(value)
value=next(g)
print(value)
value=next(g)
print(value)"""
n=sorted(g)
print(n)
# example
def countdown(num):
    print("Starting")
    while num>0:
        yield num
        num-=1
    cd = countdown(4)

    value = next(cd)
    print(value)

    print(next(cd))
    print(next(cd))
    print(next(cd))
    print(next(cd))
