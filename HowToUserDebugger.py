def test1(a, b):
    c = a/b
    return True 

def test2(a, b):
    c = a/b
    return False

if __name__ == '__main__':
    a = 1 
    b = 1 
    test1(a,b) 
    b = 0 
    test2(a,b)
    print("game over")
    