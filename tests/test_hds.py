from hds import hds

def test_one():
    x = hds()
    assert(len(x.children) == 0)
    y = hds(x)
    assert(len(y.parents) == 1)
    assert(len(x.children) == 1)

def test_two():
    x = hds()
    y = hds(x)

    x.add_data('A')
    assert(x.random() == 'a')
    assert(x.random(True) == 'a')

def test_three():
    x = hds()
    x.add_data(['a', 'b', 'c'])

    assert(x.data == ['a', 'b', 'c'])
    assert(x.random() in ['a', 'b', 'c'])

def test_four():
    x = hds()
    y = hds(x)
    y.add_data('a')
    assert(x.random() == None)
    assert(y.random() == 'a')
    assert(x.random(True) == 'a')
    assert(y.random(True) == 'a')

def test_five():
    x = hds()
    y = hds(x)
    z = hds(y)
    assert(x.random() == None)
    assert(y.random() == None)
    assert(z.random() == None)
    assert(x.random(True) == None)
    assert(y.random(True) == None)
    assert(z.random(True) == None)
    z.add_data('a')
    assert(x.random() == None)
    assert(y.random() == None)
    assert(z.random() == 'a')
    assert(x.random(True) == 'a')
    assert(y.random(True) == 'a')
    assert(z.random(True) == 'a')

def test_five():
    x = hds()
    x.add_data('a')
    y = hds(x)
    y.add_data(['b', 'c', 'd'])

    flag = False
    for i in range(1000):
        if x.random(True) == 'd':
            flag = True # really unlikely that this never happens
    assert(flag == True)

def test_six():
    x = hds()
    x.add_data('a')
    y = hds(x)
    z = hds(y)
    z.add_data(['b', 'c', 'd'])

    flag = False
    for i in range(1000):
        if x.random(True) == 'd':
            flag = True # really unlikely that this never happens
    assert(flag == True)






