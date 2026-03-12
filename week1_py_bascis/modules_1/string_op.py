def string_op(s):
    return s.upper()
    return s.lower()
    return s.title()
    return s.capitalize()


def string_op_reverse(s):
    return s[::-1]

def string_op_length(g):
    return len(g)

def count_vowels(s):
    vowels='aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def is_palindrome(s):
    cleaned=''.join(char.lower() for char in s if char.isalnum())
    return cleaned==cleaned[::-1]

    
    