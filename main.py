
from game import Game
from hangman_factory import HangManFactory 


words = [
    "teste", "camilo"]


hangMan = Game(HangManFactory())
hangMan.play()

