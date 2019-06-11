def productOfRest(array):
    productArray = []
    for i in range(len(array)):
        product = 1
        for j in range(len(array)):
            if i != j:
                product *= array[j]

        productArray.append(product)

    return productArray

def test1():
    array = [1,2,3,4,5]
    assert(productOfRest(array) == [120, 60, 40, 30, 24])

def test2():
    array = [8, 4, 2]
    assert(productOfRest(array) == [8, 16, 32])

def test3():
    array = [1, 4, -8, 0, 12]
    assert(productOfRest(array) == [0, 0, 0, -384, 0])

if __name__ == "__main__":
    test1()
    test2()
    test3()