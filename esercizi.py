def function(a):
    print(a)


# Funzione che restituisce il max tra due numeri
def max_number(a, b):
    if a > b:
        return "il massimo numero è "+str(a)
    elif a == b:
        return "I due numeri sono uguali"
    else:
        return "il massimo numero è "+str(b)


# Funzione che restituisce il max tra tre numeri
def max_three_numbers(a, b, c):
    return max(max(a, b), c)



# Funzione che restituisce il max in un elenco di numeri
def max_numbers(elenco):
    if elenco is None:
        return None
    elif type(elenco) is not list:
        return "L'input non è una lista"
    elif len(elenco) == 0:
        return "Lista vuota"
    max_i = 0
    max_n = elenco[0]
    for i, elem in enumerate(elenco[1:], 1):
        print(i, elem)
        if elem > max_n:
            max_i = i
            max_n = elem
    return elenco[max_i]


# Funzione che restituisce True se il carattere in input è una vocale, False altrimenti
def is_vocal(char):
    return char in "aeiou"


# Funzione che somma tutti gli elementi di una lista
def sum_list(elenco):
    if elenco is None:
        return None
    elif type(elenco) is not list:
        return "L'input non è una lista"
    elif len(elenco) == 0:
        return "Lista vuota"
    sum = 0
    for i, elem in enumerate(elenco):
        sum += elem
    return sum


# Funzione che moltiplica tutti gli elementi di una lista
def product_list(elenco):
    if elenco is None:
        return None
    elif type(elenco) is not list:
        return "L'input non è una lista"
    elif len(elenco) == 0:
        return "Lista vuota"
    product = 1
    for i, elem in enumerate(elenco):
        product *= elem
    return product


# Funzione che restituisce la lunghezza di una lista
def len_list(elenco):
    if elenco is None:
        return None
    elif type(elenco) is not list:
        return "L'input non è una lista"
    elif len(elenco) == 0:
        return 0
    temp = 0
    for i, elem in enumerate(elenco):
        temp = i
    return temp + 1


# Funzione che inverte una stringa
# Funzione che restituisce la lunghezza di una lista
def reverser(stringa):
    if stringa is None:
        return None
    elif type(stringa) is not str:
        return "L'input non è una lista"
    elif len(stringa) == 0:
        return "Stringa vuota"
    reverse = ""
    print(len(stringa))
    for i in range(len(stringa), 0, -1):
        reverse += stringa[i-1]
    for i, char in enumerate(stringa):
        reverse += char
    return reverse

if __name__ == '__main__':
    '''i = 10
    words = [1, 2, "ciao", 4, 5, 6]
    for i, elem in enumerate(words):
        print("Elemento numero ", i, " ",elem)
        print("ciao")

    dict = {"a": "aa", "b": "bb"}
    print(dict["a"])
    print(dict.keys())  
    print(dict.values())
    function(a=30)

    for i in range(0, 4):
        print("esercizio di prova")'''

    # Esercizio 1: Calcolare il max tra due numeri
    print(max(3, 3))
    print(max_number(2, 3))

    # Esercizio 2: Calcolare il max tra tre numeri

    # Esercizio 3: Calcolare il max in una lista
    lista = [1, 2, 3, 65, 23, 32, 45, 72, 9, 96, 3, 5, 8]
    print(max_numbers(lista))

    # Esercizio 4: dato un carattere dire se è una vocale
    print(is_vocal('a'))

    # Esercizio 5: somma tutti gli elementi di una lista
    print(sum_list([1, 2, 3, 4, 5, 6, 7]))

    # Esercizio 6: moltiplica tutti gli elementi di una lista
    print(product_list([1, 2, 3]))

    # Esercizio 7: implementare la funzione len()
    print(len_list([1, 2, 3]))

    #print(reverser("abcd"))

    a = "abcdefghi"

    print("a[0:5:-1] ", a[0:5:-1])  # all items in the array, reversed
    print("a[1::-1] ", a[1::-1])  # the first two items, reversed
    print("a[:-3:] ", a[:-3:]) # the last two items, reversed
    print("a[-2:-3:-1] ", a[:-3:-1])  # everything except the last two items, reversed

    # con step positivo, start e stop omessi indicano 0 e len(stringa)
    # con step negativo, start e stop omessi indicano len(stringa) e 0

    '''a  b  c  d  e  f  g  h  i  
       0  1  2  3  4  5  6  7  8
      -9 -8 -7 -6 -5 -4 -3 -2 -1'''

