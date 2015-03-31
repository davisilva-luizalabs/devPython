# _*_ coding: latin1 _*_

#importando o modulo string
import string

# O alfabeto
a = string.ascii_letters

# Rodando o alfabeto um caractere para a esquerda
b = a[1:] + a[0]

# A função maktrans() cria uma tabela de tradução
# entre os caracteres das duas strings que ela 
# recebeu como parametro
# Os caracteres ausentes nas tabelas serão
# copiados para a saida.

print b

tab = string.maketrans(a,b)

# A Mensagem
msg = "Esse texto será traduzido... Vai ficar bem estranho."

# A Função translate() usa a tabela de tradução
# criada pela maketrans() para traduzir uma string

print string.translate(msg,tab)
