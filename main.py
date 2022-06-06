student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# for (index, row) in data.iterrows():
#     print(row.code)
#     # pass

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    word = input("Enter the word: ")
    try:
        nato_list = [nato_dict[letter.upper()] for letter in word]
    except KeyError:
        print("Please enter alphabets only")
        generate_phonetic()
    else:
        print(nato_list)

generate_phonetic()