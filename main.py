import random

move_list = []
files = ['a', 'b','c', 'd', 'e']
file_choice = random.choice(files)

with open(f'{file_choice}.tsv', 'r') as arquivos:
    next(arquivos)
    for i in arquivos:
        moves_row = i.split('\t')
        move_list.append(moves_row[1] + " " + moves_row[2])

choice = random.choice(move_list)

print(f"Your move is: {choice}")
