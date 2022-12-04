from Utils import Validator
from Data import Dictionary


class Engine:
    attempts = None
    difficulty = None
    validator = Validator.Validator()
    dictionary = Dictionary.Dictionary()

    def __init__(self):
        self.attempts = 10
        self.difficulty = 1

    def run(self):
        stats_list = []
        counter = 0
        host_word = self.dictionary.get_random_word(self.difficulty)
        print(f"Długość wylosowanego słowa: {len(host_word)}")

        while counter < self.attempts:
            print(f"Liczba pozostałych prób: {self.attempts - counter}")
            guesser_word = self.get_user_input()

            is_valid = self.validator.validate(guesser_word, host_word)
            if not is_valid:
                print("Wprowadzone słowo jest niepoprawne")
                counter += 1
                continue

            current_attempt_stats = self.validator.calculate_bulls_and_cows_in_attempt(guesser_word, host_word)
            stats_list.append(current_attempt_stats)
            print(current_attempt_stats)

            if self.is_game_over(host_word, current_attempt_stats):
                print("Brawo! Słowo zostało odgadnięte")
                break

            counter += 1

        return stats_list

    def is_game_over(self, host_word, current_stats):
        return len(host_word) == current_stats.bulls

    def get_user_input(self):
        guesser_word = input("Twoje słowo: ")
        return str.upper(guesser_word)
