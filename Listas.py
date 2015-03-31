# _*_ coding: latin1 _*_

# Uma nova lsta : Brit progs dos anos 70
progs = ['Yes', 'Genesis', 'Pink Floyd', 'ELP']

#Verrendo a lista interia

for prog in progs:
	print prog

# Trocando o último elemento
progs[-1] = 'King Crimson'

# Incluindo
progs.append('Camel')

# Incluindo
progs.append('Davi')

# Removendo
progs.remove ('Pink Floyd')

# Ordena a Lista
progs.sort()

# Inverte a lista
progs.reverse()

# Imprime Numerado
for i, prog in enumerate(progs):
	print i + 1, '=>', prog

# Imprime do segundo item em diante
print progs [1:]