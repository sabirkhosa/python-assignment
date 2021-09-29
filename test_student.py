
from a04 import numbersToText


def test_numbersToText():
    num=1
    lang='urd'
    assert(numbersToText(num,lang))=='Aik'

def test_numbersToText1():
    num=10
    lang='urd'
    assert(numbersToText(num,lang))=='Das'

def test_numbersToText2():
    num=11
    lang='urd'
    assert(numbersToText(num,lang))=='Not Available'

def test_numbersToText3():
    num=0
    lang='eng'
    assert(numbersToText(num,lang))=='Zero'

def test_numbersToText4():
    num=0
    assert(numbersToText(num))=='Zero'


if __name__ == '__main__':
    main()
