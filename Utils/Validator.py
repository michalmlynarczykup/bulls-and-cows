class Validator:
    host_word = None

    def __init__(self, host_word):
        self.host_word = host_word

    def validate(self, guesser_word):
        if type(guesser_word) != str or not str.isalpha(guesser_word) or len(self.host_word) != len(guesser_word):
            return False

        guesser_word = str.upper(guesser_word)
        if len(guesser_word) == len(set(guesser_word)):
            return True
        return False

