import string
class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters
    def alph_letters(self):
        print(self.letters)
    def letters_num(self):
        return len(self.letters)

class EngAlphabet(Alphabet):
    def __init__(self, lang, letters):
        super().__init__(lang, letters)
        self.lang = lang
        self.letters = letters
        self.__letters_num = len(self.letters)
    def is_en_letter(self, letter):
        self.letter = letter
        if self.letter in string.ascii_letters:
            print('Это буква Английского алфавита')
        else:
            print('Это буква алфавита другого языка')
    def letters_num(self):
        return self.__letters_num
    @staticmethod
    def example():
        return 'example: He was a very talented musician.'

alphabet = Alphabet('rus', 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
alphabet.alph_letters()
print(alphabet.letters_num())
letter = EngAlphabet('En', string.ascii_uppercase)
letter.is_en_letter('F')
print(letter.letters_num())
print(EngAlphabet.example())
