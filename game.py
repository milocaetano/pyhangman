from hangman_factory import HangManFactory 
from hangman import HangMan

class Game:
    def __init__(self, hangFactory: HangManFactory):
        self.hangFactory = hangFactory

    def play(self):
        hang: HangMan = self.hangFactory.get_hangman("casa")     
        hang.print() 
