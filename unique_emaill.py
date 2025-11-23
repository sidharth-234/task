import random
import string

def generate_email_random_letters(username, domain="gmail.com"):
    letters = ''.join(random.choices(string.ascii_lowercase, k=5))
    return f"{username}.{letters}@{domain}"


for _ in range(5):
    print(generate_email_random_letters("user"))
