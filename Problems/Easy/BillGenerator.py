import random
from string import ascii_uppercase


def billGenerator():
    digits = 'MH/' + ''.join(random.choices(ascii_uppercase, k=3)) + \
             '/' + ''.join(["{}".format(random.randint(0, 9)) for num in range(0, 6)])
    print(digits)


billGenerator()
