def is_palindrome(num):
    original=num
    reversed_num=0
    while num>0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return original == reversed_num

num=int(input('enter a num:'))
if is_palindrome(num):
    print(f'{num} is palindrome')
else:
    print('not palindrome')