import random
import string


def random_generator(size=6, chars=string.ascii_letters):
    return ''.join(random.choice(chars) for x in range(size))
