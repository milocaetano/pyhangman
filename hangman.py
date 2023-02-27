import msvcrt
import os
import platform


class HangMan:

    def __init__(self, word):
        self.word = "casa".upper()
        self.charMached = []
        self.error = []

    def _addCharWithMach(self, character):
        if (character in self.word and character not in self.charMached):
            self.charMached.append(character)
        elif (character not in self.error):
            self.error.append(character)

    def _printHangMan(self):
        pass

    def _printWords(self):
        for c in self.word:
            if c in self.charMached:
                print(f" {c} ", end="")
            else:
                print(" _ ", end="")
        print()

    def print(self):
        while True:

            print("\n\n\n<<< Jogo da forca >>>\n\n")
            # Ler um caractere do teclado

            self._printWords()

            print("\n\n\nDigite um caracter:")
            caractere = msvcrt.getch().decode('utf-8')

            if platform.system() == 'Windows':
                os.system('cls')
            else:
                os.system('clear')

            # Verificar se o caractere é "esc"
            if caractere == chr(27):
                print("Saindo do loop...")
                break

            self._addCharWithMach(caractere.upper())

            # Executar alguma ação com o caractere
            print(f"O caractere digitado foi '{caractere}'")
