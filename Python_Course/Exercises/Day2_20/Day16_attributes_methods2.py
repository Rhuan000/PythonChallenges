from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ['Pokemons', 'Type']
table.add_rows(
    [
        ['Pikachu','Eletric'],
        ['Squirtle', 'Water'],
        ['Charmander','Fire'],
    ]
)
table.align = 'r'
print(table)