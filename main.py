import pandas

alphabets = False
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
while not alphabets:
    name = input("Please enter the word:\n").upper()
    alphabets = name.isalpha()
    try:
        output_list = [phonetic_dict[i] for i in name]
    except KeyError:
        print("Please enter alphabets only")
    else:
        print(output_list)
