import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
name = input("Please enter the word\n").upper()
output_list = [phonetic_dict[i] for i in name]
print(output_list)
