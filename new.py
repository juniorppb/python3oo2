class Listinha:
    def __init__(self, items):
        self.items = items

    def __iter__(self):
        return self.items.__iter__()

meu_objeto = Listinha([1, 2, 4])

contador = 0
for item in meu_objeto:
    contador += 1

if len(meu_objeto) == contador:
    print('São iguais!')
else:
    print('Não são iguais!')