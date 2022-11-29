import random
import os


class Dictionary:
    path = None

    def __init__(self):
        self.path = os.path.join(os.path.dirname(__file__), "dictionary.txt")

    def get_random_word(self, difficulty):
        if difficulty == 1:
            min_len = 1
            max_len = 3
        elif difficulty == 2:
            min_len = 3
            max_len = 5
        else:
            min_len = 5
            max_len = 20
        try:
            lines = open(self.path, 'r').read().splitlines()
            host_word = random.choice(lines)
            while min_len > len(host_word) or max_len < len(host_word):
                host_word = random.choice(lines)
            return host_word
        except IOError as e:
            print(e)
