from Data.Stats import Stats


class Validator:
    def __init__(self):
        pass

    def validate(self, guesser_word, host_word):
        if type(guesser_word) != str or not str.isalpha(guesser_word) or len(host_word) != len(guesser_word):
            return False

        if len(guesser_word) == len(set(guesser_word)):
            return True
        return False

    def calculate_bulls_and_cows_in_attempt(self, guesser_word, host_word):
        bulls = 0
        cows = 0
        for element in range(0, len(guesser_word)):
            if guesser_word[element] == host_word[element]:
                bulls += 1
            elif guesser_word[element] in host_word:
                cows += 1

        return Stats(bulls, cows)
