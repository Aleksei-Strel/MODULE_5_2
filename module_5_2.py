class HOUSE:
    def __init__(self, name, numb_f):
        self.name = name
        self.number_of_floor = numb_f

    def __len__(self):
        return self.number_of_floor


    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floor}.'

h1 = HOUSE('Скала', 28)
h2 = HOUSE('Хрущ', 5)

print((h1))
print(len(h1))
print()
print((h2))
print(len(h2))