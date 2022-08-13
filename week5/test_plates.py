from plates import is_valid

def main():
    #call test fuctions
    test_min_and_max_characters()
    test_start_with_two_letters()
    test_number_middle()
    test_number_zero()
    test_punctuation()

#plates may contain a max of 6 chars
def test_min_and_max_characters():
    assert is_valid('AA') == True
    assert is_valid('ABCDEF') == True
    assert is_valid('A') == False
    assert is_valid('ABCDEFGH') == False

#must start with at least 2 letters
def test_start_with_two_letters():
    assert is_valid('AA') == True
    assert is_valid('A2') == False
    assert is_valid('2A') == False
    assert is_valid('22') == False

#numbers cant be used in middle
def test_number_middle():
    assert is_valid('AAA222') == True
    assert is_valid('AAA22A') == False

'''
#first number cant be 0
def test_number_zero():
    assert is_valid('CS50') == True
    assert is_valid('CS05') == False


#no punctuation marks are allowed
def test_punctuation():
    assert is_valid('PI3.14') == False
    assert is_valid('PI3!14') == False
    assert is_valid('PI 14') == False

'''

if __name__ == "__main__":
    main()