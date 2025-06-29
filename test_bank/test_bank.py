from bank import value

def main():
    test_fullGreet()
    test_halfGreet()
    test_noGreet()

def test_fullGreet():
    assert value("hello") == 0
    assert value("HEllo") == 0

def test_halfGreet():
    assert value("help") == 20
    assert value("Hi") == 20
    assert value("HElp") == 20
    assert value("hi") == 20

def test_noGreet():
    assert value("balls") == 100
    assert value("apple") == 100

if __name__ == "__main__":
    main()