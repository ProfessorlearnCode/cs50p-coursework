from um import count
import pytest


def main():
    test_uppercase_lowercase()
    test_word()
    test_spaceSurround()




def test_uppercase_lowercase():
    assert count('Um, thanks for the album.') == 1
    assert count('Um, thanks um') == 2


def test_word():
    assert count('Yummy') == 0

def test_spaceSurround():
    assert count('um?') == 1
    assert count('Hello um World') == 1


if __name__ == "__main__":
    main()
