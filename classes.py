import itertools
import json
import os
import random
import sys

dictionary = {"Α": [], "Β": [], "Γ": [], "Δ": [], "Ε": [], "Ζ": [], "Η": [], "Θ": [], "Ι": [], "Κ": [], "Λ": [],
              "Μ": [], "Ν": [], "Ξ": [], "Ο": [], "Π": [], "Ρ": [], "Σ": [], "Τ": [], "Υ": [], "Φ": [], "Χ": [],
              "Ψ": [], "Ω": []}


class SakClass:
    def __init__(self):
        self.sack = []
        self.__Values_of_Letters = {"Α": 1, "Β": 8, "Γ": 4, "Δ": 4, "Ε": 1, "Ζ": 10, "Η": 1, "Θ": 10, "Ι": 1, "Κ": 2,
                                    "Λ": 3, "Μ": 3, "Ν": 1, "Ξ": 10, "Ο": 1, "Π": 2, "Ρ": 2, "Σ": 1, "Τ": 1, "Υ": 2,
                                    "Φ": 8, "Χ": 8, "Ψ": 10, "Ω": 3, }

        self.__Number_of_Letters = {"Α": 12, "Β": 1, "Γ": 2, "Δ": 2, "Ε": 8, "Ζ": 1, "Η": 7, "Θ": 1, "Ι": 8, "Κ": 4,
                                    "Λ": 3, "Μ": 3, "Ν": 6, "Ξ": 1, "Ο": 9, "Π": 4, "Ρ": 5, "Σ": 7, "Τ": 8, "Υ": 4,
                                    "Φ": 1, "Χ": 1, "Ψ": 1, "Ω": 3}

        self.__Letters = ["Α", "Β", "Γ", "Δ", "Ε", "Ζ", "Η", "Θ", "Ι", "Κ", "Λ", "Μ", "Ν", "Ξ", "Ο", "Π", "Ρ", "Σ", "Τ",
                          "Υ", "Φ", "Χ", "Ψ", "Ω"]
        self.__randomize_sak()

    def __randomize_sak(self):
        for value in self.__Number_of_Letters.values():
            self.sack.append(value)

    def get_letters(self):
        return self.__Letters

    def get_letter_point(self, letter):
        return self.__Values_of_Letters[letter]

    def word_exists(self, word):
        for letter in word:
            if letter not in self.__Letters:
                return False
        if word in dictionary[word[0]]:
            return True
        return False

    def getletters(self, n):
        letters = list()
        for i in range(n):
            rand = random.randint(0, len(self.sack)-1)

            while self.sack[rand] == 0:
                rand = random.randint(0, len(self.sack)-1)

            letters.append(self.__Letters[rand])
            self.sack[rand] -= 1
        return letters

    def putbackletters(self, letters):
        for letter in letters:
            self.sack[self.__Letters.index(letter)] += 1

    def get_num_remaining(self):
        counter = 0
        for value in self.sack:
            counter += value

        return counter


class Player:
    def __init__(self):
        self._letters = []
        self._points = 0
        self._sak = SakClass()

    def __repr__(self):
        return f'Class: {self.__class__}, letters: {self._letters}, points: {self._points}'

    def set_letters(self, letters):
        self._letters = list(letters)

    def reroll_letters(self, sak, temp_letters):
        self._sak = sak
        flag, no_of_letters = self.check_remaining_letters(self._sak, 7)
        if flag:
            new_set_of_letters = self._sak.getletters(7)
            self._sak.putbackletters(temp_letters)
            self._letters = list(new_set_of_letters)
            return True
        elif no_of_letters >= 2:
            new_set_of_letters = self._sak.getletters(no_of_letters)
            self._sak.putbackletters(temp_letters)
            self._letters = list(new_set_of_letters)
            return True
        else:
            print("Not enough letters remaining in the sack to re-roll!")
            return False

    def add_points(self, word, temp_letters):
        counter = 0
        for letter in word.upper():
            counter += self._sak.get_letter_point(letter)
        self._points += counter
        self._letters = list(temp_letters)
        flag = True
        flag1, no_of_letters = self.check_remaining_letters(self._sak, 7 - len(self._letters))
        if flag1:
            new_set_of_letters = self._sak.getletters(7 - len(self._letters))
            for letter in new_set_of_letters:
                self._letters.append(letter)
            flag = False
        elif no_of_letters >= 2:
            new_set_of_letters = self._sak.getletters(self._sak.get_num_remaining())
            for letter in new_set_of_letters:
                self._letters.append(letter)
            flag = False
        return counter, flag

    def check_remaining_letters(self, sak, number):
        self._sak = sak
        if self._sak.get_num_remaining() < number:
            return False, self._sak.get_num_remaining()
        return True, number

    def check_valid_word_existence(self):
        for i in range(2, len(self._letters)):
            temp_letters = str()
            for x in self._letters:
                temp_letters += x
            permutations = [''.join(j) for j in itertools.permutations(temp_letters, i)]

            for permutation in permutations:
                if self._sak.word_exists(permutation):
                    return True
        return False

    def get_letters(self):
        return self._letters

    def get_points(self):
        return self._points

    @staticmethod
    def form_answer(sak, letters, player):
        var = str()
        if player == "Human":
            print("In bag: " + str(sak.get_num_remaining()) + " letters - Your turn:\nAvailable letters: \n| " +
                  ' '.join(str(x) + ": " + str(sak.get_letter_point(x)) + " |" for x in letters))
        elif player == "PC":
            print("In bag: " + str(sak.get_num_remaining()) + " letters - PC turn:" + var + "\nPC letters: " +
                  ' '.join(str(x) + ": " + str(sak.get_letter_point(x)) + " |" for x in letters))


class Human(Player):
    def __init__(self):
        super().__init__()
        self.__temp_letters = str()

    def play(self, sak):
        self._sak = sak

        word = input("Input (type h for help if you don't remember one of the commands): ")
        while True:
            while True:
                if word == "" or (self.__validate_word(word.upper()) and self._sak.word_exists(word.upper())) or \
                        word == 'p' or word == 'q' or word == "c" or word == "h":
                    break
                else:
                    if not self.__validate_word(word.upper()):
                        word = input("Type a word only with letters you own: ")
                    elif not self._sak.word_exists(word.upper()):
                        word = input("The word doesn't exist. Please, type a new one: ")
                    else:
                        word = input("Invalid word, please try again: ")

            if word != 'p' and word != 'q' and word != '' and word != "c" and word != "h":
                counter, flag = self.add_points(word, self.__temp_letters)
                print("Valid word - Points earned: " + str(counter) + " - Score: " + str(self._points))
                if not flag:
                    input("Press enter to continue...")
                    print("--------------------------")
                    return self._sak, True
                else:
                    input("Not enough letters in the bag to fill out the number of used letters! Press enter to "
                          "continue...")
                    print("--------------------------")
                    return self._sak, False
            elif word == 'p':
                if self.reroll_letters(self._sak, self.__temp_letters):
                    print("Rerolled! New letters: ")
                else:
                    print("Press \"q\" if you want to end the game. Letters: ")
                print("| " + ' '.join(str(x) + ": " + str(self._sak.get_letter_point(x)) + " |" for x in self._letters))
            elif word == 'q':
                return self._sak, False
            elif word == "c":
                if self.check_valid_word_existence():
                    print("There is a valid word with your current letters!")
                else:
                    print("There isn't a valid word with your current letters! You could reroll you letters (p) or quit"
                          " the game (q)!")
            elif word == "h":
                print("\nCommands:\np: Re-roll letters\nc: Check if there is a valid word with the letters you own\nh: "
                      "Help\nq: Quit")

            word = input("Input (type h for help if you don't remember one of the commands): ")

    def __validate_word(self, word):
        self.__temp_letters = list(self._letters)
        for letter in word:
            if letter in self.__temp_letters:
                self.__temp_letters.remove(letter)
            else:
                return False
        return True


class Computer(Player):
    def __init__(self, mode):
        super().__init__()
        self.__temp_letters = str()
        self.__mode = mode

    def play(self, sak, mode):
        self._sak = sak
        self.__mode = mode
        if self.__mode == "MIN":
            return self._sak, self.__min_mode()
        elif self.__mode == "MAX":
            return self._sak, self.__max_mode()
        elif self.__mode == "SMART":
            return self._sak, self.__smart_mode()

    def __min_mode(self):
        self.__temp_letters = str()
        for x in self._letters:
            self.__temp_letters += x

        if not self.check_valid_word_existence():
            print("Pc couldn't find a valid word! Re-rolling once!")
            if self.reroll_letters(self._sak, self._letters):
                if not self.check_valid_word_existence():
                    print("Pc couldn't find a word again!")
                    return False
            else:
                return False

        for i in range(2, len(self._letters)):
            permutations = [''.join(j) for j in itertools.permutations(self.__temp_letters, i)]

            for permutation in permutations:
                if self._sak.word_exists(permutation):
                    self.form_answer(self._sak, self._letters, "PC")
                    for letter in permutation:
                        self._letters.remove(letter)
                    counter, flag = self.add_points(permutation, self._letters)
                    print("Word: " + permutation + " - Points earned: " + str(counter) + " - Score: " +
                          str(self._points))
                    if not flag:
                        input("Press enter to continue...")
                        print("--------------------------")
                    else:
                        input("Not enough letters in the bag to fill out the number of used letters! Press enter to "
                              "continue...")
                        print("--------------------------")
                        return False
                    return True

    def __max_mode(self):
        self.__temp_letters = str()
        for x in self._letters:
            self.__temp_letters += x

        if not self.check_valid_word_existence():
            print("Pc couldn't find a valid word! Re-rolling once!")
            if self.reroll_letters(self._sak, self._letters):
                if not self.check_valid_word_existence():
                    print("Pc couldn't find a word again!")
                    return False
            else:
                return False

        for i in range(len(self._letters), 1, -1):
            permutations = [''.join(j) for j in itertools.permutations(self.__temp_letters, i)]

            for permutation in permutations:
                if self._sak.word_exists(permutation):
                    self.form_answer(self._sak, self._letters, "PC")
                    for letter in permutation:
                        self._letters.remove(letter)
                    counter, flag = self.add_points(permutation, self._letters)
                    print("Word: " + permutation + " - Points earned: " + str(counter) + " - Score: " + str(
                        self._points))
                    if not flag:
                        input("Press enter to continue...")
                        print("--------------------------")
                    else:
                        input("Not enough letters in the bag to fill out the number of used letters! Press enter to "
                              "continue...")
                        print("--------------------------")
                        return False
                    return True

    def __smart_mode(self):
        self.__temp_letters = str()
        for x in self._letters:
            self.__temp_letters += x

        temp_word = str()
        temp_points = 0

        if not self.check_valid_word_existence():
            print("Pc couldn't find a valid word! Re-rolling once!")
            if self.reroll_letters(self._sak, self._letters):
                if not self.check_valid_word_existence():
                    print("Pc couldn't find a word again!")
                    return False
            else:
                return False

        for i in range(2, len(self._letters)):
            permutations = [''.join(j) for j in itertools.permutations(self.__temp_letters, i)]

            for permutation in permutations:
                if self._sak.word_exists(permutation):
                    counter = 0
                    for letter in permutation.upper():
                        counter += self._sak.get_letter_point(letter)
                    if counter > temp_points:
                        temp_points = counter
                        temp_word = str(permutation)

        self.form_answer(self._sak, self._letters, "PC")
        for letter in temp_word:
            self._letters.remove(letter)
        counter, flag = self.add_points(temp_word, self._letters)
        print("Word: " + temp_word + " - Points earned: " + str(counter) + " - Score: " + str(self._points))
        if not flag:
            input("Press enter to continue...")
            print("--------------------------")
        else:
            input("Not enough letters in the bag to fill out the number of used letters! Press enter to continue...")
            print("--------------------------")
            return False
        return True


class Game:
    def __init__(self):
        self.__modes = ["MIN", "MAX", "SMART"]
        self.__current_mode = "ΜΙΝ"
        self.__score_file_path = "DataScoreFile.json"
        self.__word_file_path = "greek7.txt"

        self.__create_dictionary(self.__word_file_path)
        self.__sak = SakClass()
        self.__player = Human()
        self.__computer = Computer(self.__current_mode)

    def __repr__(self):
        return f'Class: {self.__class__}, modes: {self.__modes}, current mode: {self.__current_mode}, ' \
               f'player: ({repr(self.__player)}), computer: ({repr(self.__computer)})'

    def __setup(self):
        print("SETTINGS\nThere are 3 modes of PC (MIN is the default one):\n1: MIN\n2: MAX\n3: SMART\nq: Quit")
        user_input = input("Enter the the correct input to change mode or quit the settings menu: ")
        while user_input != "Quit" and user_input != "q":
            if user_input == "MIN" or user_input == "1":
                if self.__current_mode != "MIN":
                    self.__current_mode = self.__modes[0]
                    print("Current mode changed to " + self.__modes[0] + ".")
                else:
                    print("Current mode is already " + self.__modes[0] + ".")
            elif user_input == "MAX" or user_input == "2":
                if self.__current_mode != "MAX":
                    self.__current_mode = self.__modes[1]
                    print("Current mode changed to " + self.__modes[1] + ".")
                else:
                    print("Current mode is already " + self.__modes[1] + ".")
            elif user_input == "SMART" or user_input == "3":
                if self.__current_mode != "SMART":
                    self.__current_mode = self.__modes[2]
                    print("Current mode changed to " + self.__modes[2] + ".")
                else:
                    print("Current mode is already " + self.__modes[2] + ".")
            user_input = input("Enter the mode name or type \"Quit\" or \"q\" to quit the settings menu: ")

    def run(self):
        user_input = input("Welcome to the Scrabble game!\n1: Start\n2: Settings\n3: Previous Results\nq: Quit\nType "
                           "the correct input to navigate to the section that you want: ")
        print("--------------------------")

        while user_input != "Start" and user_input != "1":
            if user_input == "Settings" or user_input == "2":
                self.__setup()
                print("--------------------------")
            elif user_input == "Previous Results" or user_input == "3":
                self.__show_previous_results()
            elif user_input == "Quit" or user_input == "q":
                self.__end()
            else:
                print("Invalid input!")
            user_input = input("1: Start\n2: Settings\n3: Previous Results\nq: Quit\nType the correct input to "
                               "navigate to the section that you want: ")
            print("--------------------------")

        letters_player = self.__sak.getletters(7)
        self.__player.set_letters(letters_player)

        letters_pc = self.__sak.getletters(7)
        self.__computer.set_letters(letters_pc)

        flag = True
        while flag:
            self.__player.form_answer(self.__sak, self.__player.get_letters(), "Human")
            self.__sak, flag = self.__player.play(self.__sak)
            if not flag:
                self.__end()
            self.__sak, flag = self.__computer.play(self.__sak, self.__current_mode)
            if not flag:
                self.__end()

    def __end(self):
        if self.__player.get_points() == self.__computer.get_points() == len(self.__computer.get_letters()) == \
                len(self.__player.get_letters()) == 0:
            print("Game didn't start so there is no result!")
            sys.exit()
        elif self.__player.get_points() > self.__computer.get_points():
            print("Player wins!")
        elif self.__player.get_points() < self.__computer.get_points():
            print("Computer wins!")
        else:
            print("Tie!")

        print("Game ends\nPlayer points: " + str(self.__player.get_points()) + ", PC points: " +
              str(self.__computer.get_points()) + ".")
        self.__update_score_data(self.__score_file_path, self.__player.get_points(), self.__computer.get_points())
        sys.exit()

    def __show_previous_results(self):
        score_data = self.__load_score_data(self.__score_file_path)
        if score_data == "Empty file":
            print("There are no previous game records!\n--------------------------")
        else:
            counter = 1
            for entry in score_data.values():
                print("Game " + str(counter) + " score:\nPlayer score: " + str(entry[0]) + "\nComputer score: " +
                      str(entry[1]))
                if entry[0] > entry[1]:
                    print("Player won game " + str(counter) + "!")
                elif entry[0] < entry[1]:
                    print("Computer won game " + str(counter) + "!")
                else:
                    print("Game " + str(counter) + " ended with a tie!")
                print("--------------------------")
                counter += 1

    @staticmethod
    def __load_score_data(path):
        if os.path.getsize(path) != 0:
            with open(path, 'r') as file:
                score_data = json.load(file)
            file.close()
            return score_data
        else:
            return "Empty file"

    def __update_score_data(self, path, player_score, pc_score):
        data = self.__load_score_data(path)
        if data == "Empty file":
            data = {"0": [player_score, pc_score]}
            with open(path, 'w') as file:
                json.dump(data, file)
            file.close()
        else:
            data.update({str(len(data)): [player_score, pc_score]})
            with open(path, 'w') as file:
                json.dump(data, file)
            file.close()

    @staticmethod
    def __create_dictionary(path):
        with open(path, encoding="utf8") as file:
            line = file.readline()
            while line:
                dictionary[str(line[0])] += [line.strip("\n")]
                line = file.readline()
        file.close()
