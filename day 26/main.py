# old_list = [1, 2, 3]
# new_list = [n+1 for n in old_list]
# print(new_list)
# name = "Angela"
# letter_list = [n for n in name]
# print(letter_list)
# new_range = range(1, 6)
# new_range_list = [n*2 for n in new_range]
# print(new_range_list)
# name_list = ["Alinor", "Abibi", "bibi"]
# new_name_list = [n.upper() for n in name_list if len(n) > 5]
# print(new_name_list)

# dict_student = {"one": 68,
#                 "two": 51,
#                 "three": 28}
# passed_student = {key: value for (key, value) in dict_student.items() if value > 50}
# print(passed_student)

import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row.letter:row.code for (index, row) in data.iterrows()}
word = input("please write word you want to read: ").upper()
return_list = [new_dict[letter] for letter in word]
print(return_list)



# word = input("please enter word: ")
# return_list = []
# new_dict = {index:row for (index, row) in data.iterrows()}
# print(new_dict)


