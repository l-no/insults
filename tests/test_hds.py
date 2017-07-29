from hds import hds

def test_ith_recursive():
    x = hds()
    x.data = ['a', 'b', 'c', 'd', 'e', 'f']
    y = hds(x)
    y.data = ['g', 'h', 'i', 'j', 'k', 'l']
    z = hds(x)
    z.data = ['m', 'n']

    for i in range(13):
        r = x.get_ith_recursive(i)
        assert(r == chr(i + ord('a')))

    w = hds(y)
    w.data = ['0', '1', '2']
    assert(   x.get_ith_recursive(12)
           == y.get_ith_recursive(6)
           == w.get_ith_recursive(0)
           == '0')
    assert(   x.get_ith_recursive(13)
           == y.get_ith_recursive(7)
           == w.get_ith_recursive(1)
           == '1')
    assert(   x.get_ith_recursive(14)
           == y.get_ith_recursive(8)
           == w.get_ith_recursive(2)
           == '2')

def test_total_elements_recursive():
    x = hds()
    x.data = ['a', 'b', 'c', 'd', 'e', 'f']
    y = hds(x)
    y.data = ['g', 'h', 'i', 'j', 'k', 'l']
    z = hds(x)
    z.data = ['m', 'n']
    w = hds(y)
    w.data = ['o', 'p']

    assert(z.get_total_elements_recursive() == 2)
    assert(w.get_total_elements_recursive() == 2)
    assert(y.get_total_elements_recursive() == 8)
    assert(x.get_total_elements_recursive() == 16)



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
            flag = True # really unlikely that this doesn't happens
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
            flag = True # really unlikely that this doesn't happens
    assert(flag == True)

# TODO more tests? tests 5 and 6 are more focused on the old hds system


