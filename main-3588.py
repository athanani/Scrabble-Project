import classes
game = classes.Game()
game.run()





# def check_valid_word_existence(letters):
#
#     for i in range(2, len(letters)):
#         temp_letters = str()
#         for x in letters:
#             temp_letters += x
#         permutations = [''.join(j) for j in itertools.permutations(temp_letters, i)]
#
#         for permutation in permutations:
#             print(permutation)
#             if word_exists(permutation):
#                 return True
#     return False
#
# def word_exists(word):
#     for letter in word:
#         if letter not in classes.Letters:
#             return False
#     if word in classes.dictionary[word[0]]:
#         return True
#     return False
#
# temp_letters = ['Γ', 'Κ', 'Κ', 'Σ', 'Μ', 'Δ', 'Μ']
#
# print(check_valid_word_existence(temp_letters))