from twttr import shorten

def main():
    test_upper()
    test_upper()
    test_mixed_cases()
    test_numbers()
    test_punctuation()

def test_lower():
    assert shorten("twitter") == "twttr"
def test_upper():
    assert shorten("TWITTER") == "TWTTR"
def test_mixed_cases():
    assert shorten("tWiTteR") == "tWTtR"
def test_numbers():
    assert shorten("1234") == "1234"
def test_punctuation():
    assert shorten("!,.?") == "!,.?"

if __name__ == "__main__":
    main()