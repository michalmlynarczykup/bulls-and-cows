import random
import os


class Dictionary:
    def __init__(self):
        print(self)

    path = os.path.join(os.path.dirname(__file__), "dictionary.txt")

    def get_random_word(self):
        try:
            lines = open(self.path, 'r').read().splitlines()
            return random.choice(lines)
        except IOError as e:
            print(e)
