# _*_ coding: latin1 _*_
# Fatorial implementado de forma recursiva

def fatorial(num):

	if num <= 1:
		return 1
	else:
		return(num * fatorial (num - 1))

# Testando fatorial()
print fatorial(5)


def fatorial (n):

	n = n if n > 1 else 1

	j = 1
	
	for i in range (1, n + 1):
		j = j * i
	return j

# Testando
for i in range (1,6):
	print i, '->', fatorial (i)


def fib (n):
	"""Fibonacci:
	fib(n) = fib(n - 1) + fib(n -2) se n > 1
	fib(n) = 1 se n < = 1
	"""

	if n > 1:
		return fib(n - 1) + fib(n - 2)
	else:
		return 1

# Mostra Fibonacci de 1 a 5
for i in [1,2,3,4,5]:
	print i, '=>', fib(i)
