"""generates a list of palindromes, converts to string and checks if its reversible"""


def is_palindrome(num):
    if str(num) == str(num[::-1]):
        return True


def all_palindromes():
    find_palindrome = []
    for a in range(100, 999):
        for b in range(100, 999):
            p = str(b * a)
            if is_palindrome(p):
                find_palindrome.append(b * a)
    return find_palindrome


print(max(all_palindromes()))

"""prints largest palindrome in the list"""
