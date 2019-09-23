"""generates a list of palindromes, converts to string and checks if its reversible"""

find_palindrome = []
for a in range(100, 999):
    for b in range(100, 999):
        num = str(b * a).split()[0]
        if str(num) == str(num[::-1]):
            find_palindrome.append(b * a)
print(max(find_palindrome))

"""prints largest palindrome in the list"""
