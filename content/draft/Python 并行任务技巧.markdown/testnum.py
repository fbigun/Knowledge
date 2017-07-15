def test(f, a, b):
    print('test')
    print(f(a, b))


test((lambda x,y: x**2 + y), 6, 9)


re = map((lambda x: x+3),[1,3,5,6])

resu = map((lambda x,y: x+y),[1,2,3],[6,7,9])
