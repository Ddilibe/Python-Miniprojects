# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word):
    """
    >>> find_anagrams("racecar")
    True
    >>> find_anagrams("Expression")
    False
    """
    # [assignment] Add your code here
    first = word
    try:
        second = list(word)
        third = []
        for i in range(1, len(word)+1):
            third.append(str(second[-i]))
        third=''.join(third)
        if third == first:
            return True
        else:
            return False
    except TypeError:
        print("Not able to  convert into a list")


