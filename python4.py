a = 999
b = 999
reverse_palindrome = potential_palindrome[::-1]
for i in range (1000):
    potential_palindrome = a*b
    if int((potential_palindrome == reverse_palindrome)):
        print(potential_palindrome)
