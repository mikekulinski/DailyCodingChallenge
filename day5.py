def cons(a, b):
    def pair(f):
        return f(a, b)

    return pair


def get_first(a, b):
    if(type(a) == int):
        return a
    else:
        return car(a)


def get_last(a, b):
    if(type(b) == int):
        return b
    else:
        return cdr(b)


def car(pair):
    return pair(get_first)


def cdr(pair):
    return pair(get_last)


def test1():
    pair1 = cons(4, 5)
    pair2 = cons(pair1, 8)
    assert(car(pair2) == 4)
    assert(cdr(pair2) == 8)
    assert(cdr(pair1) == 5)


def test2():
    pair1 = cons(5, 7)
    pair2 = cons(cdr(pair1), -4)
    assert(cdr(pair2) == -4)
    assert(car(pair2) == 7)


if __name__ == "__main__":
    test1()
    test2()
