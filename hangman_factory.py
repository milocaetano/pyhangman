from hangman import HangMan

class HangManFactory :

    def get_hangman(self, word):
        return HangMan(word)