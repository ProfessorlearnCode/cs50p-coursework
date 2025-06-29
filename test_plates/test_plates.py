from plates import is_valid
def main():
    test_MaxMin()
    test_startingLetters()
    test_number_placement()
    test_punctuation_zero()
    test_alnum()

def test_startingLetters():
    assert is_valid("C5S5") == False
    assert is_valid("44S5") == False
    assert is_valid("!!CS5") == False

def test_MaxMin():
    assert is_valid("ECTO88") == True
    assert is_valid("CS") == True
    assert is_valid("CSS550AA") == False
    assert is_valid("A") == False
    assert is_valid("A0") == False
    assert is_valid("A-") == False

def test_number_placement():
    assert is_valid("AAA444") == True
    assert is_valid("AAA44A") == False
    assert is_valid("0000") == False
    assert is_valid("CS05") == False
    assert is_valid("AAAAAA") == True

def test_punctuation_zero():
    assert is_valid('PI 3.14') == False
    assert is_valid('PI!3.14') == False
    assert is_valid('PI!314') == False
    assert is_valid("PI@$03") == False
    assert is_valid("@$03") == False

def test_alnum():
    assert is_valid("CS50") == True
    assert is_valid("50") == False


if __name__ == "__main__":
    main()