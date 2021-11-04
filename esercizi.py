import xlrd
import re
import random
import string
import platform
import os
import smtplib
import shutil


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


# Funzione che verifica se una parola è palindroma o meno
def is_palindroma(word):
    cursor = int((len(word)/2))
    print(cursor)
    #if len(word) % 2 == 0:
    #    cursor = int(len(word)/2)
    #else:
    #    cursor = int((len(word)/2)+1)
    for i in range(0, cursor):
        print(i)
        print(word[i], word[len(word)-1-i])
        if word[i] != word[len(word)-i-1]:
            return False
    return True


# Funzione "smart" che verifica se una parola è palindroma o meno
def smart_is_palindroma(word):
    reverse_word = word[::-1]
    return reverse_word==word


# Funzione che genera istogrammi di *
def istogram_generator(elenco):
    for i, elem in enumerate(elenco):
        stringa = ""
        for j in range(0, elem):
            stringa += "*"
        print(elem, stringa)
        print("*" * elem)
    return


# Funzione che restituisce elenco delle lunghezze delle stringhe di una lista
def len_words(elenco):
    elenco_len = []
    for i, elem in enumerate(elenco):
        elenco_len.append(len(elem))
    return elenco_len


# Funzione per calcolare frequenza lettere in una stringa
def frequenzimetro(word):
    print(word)
    dict = {}
    for i, elem in enumerate(word):
        if elem not in dict:
            dict[elem] = 1
        else:
            dict[elem] = dict[elem] + 1
    print(dict)
    #for i, elem in enumerate(word):
    #    dict[elem] = dict[elem]+1
    #print(dict)
    return dict


# Verificare se un elemento è in una lsta e restituire l'indice
def check_elem(elem, list):
    for i, value in enumerate(list):
        if elem == value:
            return (f"Il valore {elem} è presente nella lista in posizione {i}")
    return (f"Il valore {elem} non è presente nella lista")
    #return list.index(elem)


# Funzione che implementa il linguaggio rovarspraket
def rovarspraket(word):
    temp = word
    while True:
        translate = ""
        print(temp)
        for i, elem in enumerate(temp):
            if elem in "aeiou" or elem == " ":
                translate += elem
            else:
                translate += elem + "o" + elem
        print(translate)
        temp = ""
        while temp == "":
            answer = input("Vuoi tradurre un'altra frase? s/n \n")
            if answer == "n":
                return
            temp = input("Inserisci la frase")


# Funzione che legge file excel e memorizza le righe in una lista
def read_excel(file_name):
    loc = file_name
    # To open Workbook
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    nrows = sheet.nrows
    ncols = sheet.ncols
    intestazioni = []
    for i in range(0, 3):
        intestazioni.append(sheet.cell_value(0, i))
    print(intestazioni)

    elements = []
    for i in range(1, nrows):
        element = []
        for j, field in enumerate(intestazioni):
            valore = sheet.cell_value(i, j)
            #if j==0:
            #    valore = re.sub(r' \[.*?\]', '', str(sheet.cell_value(i, j)))
            element.append((field, valore))
        elements.append(element)

    return elements


# Funzione che data una lista di elementi, converte ogni elemento in una riga di un file testuale
def write_txt(elements, txt_name):
    line = ""
    file_txt = open(txt_name, "a")
    for elem in elements:
        i = 0
        for value in elem:
            if i == 0:
                # file_txt.write("("+str(value[0])+":"+str(value[1])+");")
                file_txt.write(str(value[1]) + ";")
                line += str(value[1]) + ";"
            elif i == 2:
                # file_txt.write("("+str(value[0])+":"+str(value[1])+")")
                file_txt.write(str(value[1]))
                line += str(value[1]) + ";"
            i += 1
        # file_txt.write(str(value[1]))
        file_txt.write("\n")

    file_txt.close()


# Esercizio bonus: scrivere una funzione che converte un file excel in un file txt
def excel_to_txt(file_name):
    elements = read_excel(file_name)
    txt_name = "db_alimenti.txt"
    write_txt(elements, txt_name)


# Funzione che definisce una lista di elementi simili per KCal
def def_similarity_list(elements):
    new_element = []
    new_elements = []

    for i, elem in enumerate(elements):
        temp_list = []
        temp_list.append(elem[0][1].lower())
        # print(elem)
        temp_list.append(int(elem[2][1]))
        for j, elem2 in enumerate(elements):
            if len(temp_list) == 5:
                break
            # if elem2[2][1] >= (float(elem[2][1])- 5.0) and elem2[2][1] <= (elem[2][1]+ 5) and elem[0][1] != elem2[0][1]:
            if elem2[2][1] == float(elem[2][1]) and elem[0][1] != elem2[0][1]:
                temp_list.append(elem2[0][1].lower())
        if len(temp_list) != 2:
            new_elements.append(temp_list)

    #print(len(new_elements))
    return new_elements


# Funzione che converte una lista di valori in una stringa
def list_to_string(new_elements):
    new_elements_string = []
    for j, elem in enumerate(new_elements):
        i = 0
        str_elem = ""
        # file_txt.write(str(j)+";")
        for value in elem:
            if i != len(elem) - 1:
                # file_txt.write("("+str(value[0])+":"+str(value[1])+");")
                # file_txt.write(value + ";")
                str_elem += str(value) + ";"
            elif i == len(elem) - 1:
                # file_txt.write("("+str(value[0])+":"+str(value[1])+")")
                # file_txt.write(value)
                str_elem += str(value)
            i += 1
        # print(str_elem)
        new_elements_string.append(str_elem)
    return new_elements_string


# Funzione che converte gli elementi di una lista in un file txt e formatta le righe
# (tutte le righe hanno la stessa lunghezza)
def write_txt_format_row(new_elements_string, new_elements, filler_char):
    max = 0
    len_list = []
    for elem in new_elements_string:
        # print(elem, len(elem))
        len_list.append(len(elem))
        if len(elem) > max:
            # print(len(elem))
            max = len(elem)
    print("valore max", max)

    file_txt = open("similarità.txt", "a")
    for j, elem in enumerate(new_elements):
        i = 0
        # file_txt.write(str(j)+";")
        for value in elem:
            if i != len(elem) - 1:
                # file_txt.write("("+str(value[0])+":"+str(value[1])+");")
                file_txt.write(str(value) + ";")
            elif i == len(elem) - 1:
                # file_txt.write("("+str(value[0])+":"+str(value[1])+")")
                file_txt.write(str(value))
            i += 1
        line_len = len_list[j]
        temp = line_len
        while temp < max:
            file_txt.write(filler_char)
            temp += 1
        file_txt.write("\n")

    file_txt.close()


def similarity_list(file_name):
    elements = read_excel(file_name)
    new_elements = def_similarity_list(elements)
    new_elements_string = list_to_string(new_elements)
    filler_char = "!"
    write_txt_format_row(new_elements_string, new_elements, filler_char)


# Funzione di supporto che verificare se una stringa può essere convertita in float e se è un numero maggiore di 0
def is_positive_number(s):
    try:
        num = float(s)
        if num < 0.0:
            print("Non si accettano numeri negativi!")
            return False
        return True
    except ValueError:
        if s != "":
            print("Il valore inserito non è un numero!")
        return False


def area_quadrato():
    answer = ""
    while not is_positive_number(answer):
        answer = input(
                "Inserisci lato quadrato \n")
    lato = float(answer)
    #print(lato*lato)
    return lato*lato


def area_rettangolo():
    base = float(input(
        "Inserisci base rettangolo \n"))
    altezza = float(input(
        "Inserisci altezza rettangolo \n"))
    return base*altezza


def area_cerchio():
    raggio = float(input(
        "Inserisci raggio cerchio \n"))
    return 2*raggio*3.14


def area_triangolo():
    base = float(input(
        "Inserisci base triangolo \n"))
    altezza = float(input(
        "Inserisci altezza triangoo \n"))
    return (base*altezza)/2


# Definizione switch-case tramite dizionario
def switch_demo(argument):
    switcher = {
        "quadrato": 1,
        "rettangolo": 2,
        "cerchio": 3,
        "triangolo": 4
    }
    return switcher.get(argument, "Forma non valida")


# Funzione che calcola l'area di una forma in base all'input fornito dall'utente
def calc_area(forma):
    answer = switch_demo(forma)
    if answer == 1:
        return "L'area del {} è uguale a {}.".format(forma, area_quadrato())
    elif answer == 2:
        return "L'area del {} è uguale a {}.".format(forma, area_rettangolo())
    elif answer == 3:
        return "L'area del {} è uguale a {}.".format(forma, area_cerchio())
    elif answer == 4:
        return "L'area del {} è uguale a {}.".format(forma, area_triangolo())
    print("Forma non valida")
    return -1


# Funzione che converte una misura in metri in una scala a scelta
def convert(value, index):
    if index == 1:
        return value * 1.09361
    elif index == 2:
        return value * 39.3701
    elif index == 3:
        return value * 3.28084
    elif index == 4:
        return value * 0.000621371
    return "Misurazione non valida"


# Funzione che converte una misura in metri in quattro scale diverse
def convert2(value):
    converter = {
        "iarde": value * 1.09361,
        "pollici": value * 39.3701,
        "piedi": value * 3.28084,
        "miglia": value / 1609.344
    }

    for key in converter.keys():
        print("{} metri equivalgono a {} {}".format(value, converter[key], key))


# Funzione che converte giorni, ore e minuti in un totale di secondi
def time_in_seconds(days, hours, minutes):
    return (days * 24 * 60 * 60) + (hours * 60 * 60) + (minutes * 60)


# Funzione che genera una password di 8 caratteri
def soft_pwd():
    pwd = ""
    for i in range(8):
        num = random.randint(33, 122)
        pwd += chr(num)
    return pwd


# Funzione che genera un indirizzo MAC
def gen_MAC():
    mac_address = ""
    for _ in range(5):
        exa_0x = str(hex(random.randint(0, 255)))
        exa = exa_0x.replace("0x", "")
        mac_address += exa + ":"
    exa_0x = str(hex(random.randint(0, 255)))
    exa = exa_0x.replace("0x", "")
    mac_address += exa
    return mac_address


# Funzione alternativa per generare indirizzo MAC
def genera_mac():
    char_set = "ABCDEF0123456789"
    mac_addr = ""
    due_punti = 0

    for _ in range(6):
        for _ in range(2):
            mac_addr += random.choice(char_set)
        if due_punti < 5:
          mac_addr += ":"
          due_punti += 1

    return mac_addr


# Funzione che dato un elenco di parole e una parola in input trova tutte le parole che fanno rima con l'input
# (ultime tre lettere uguali)
def rimario(word, list):
    sim_list = []
    for elem in list:
        print(word[-3:], elem[-3:])
        if word[-3:] == elem[-3:]:
            sim_list.append(elem)
    return sim_list


order_list = []


# Funzione che verifica se un libro è presente in libreria, decrementa il num di copie in caso di vendita
def vendi_libri(library, book_name):
    book_name_lower = book_name.lower()
    if book_name_lower not in library:
        order_list.append(book_name_lower)
        return False, "Mi dispiace ma il libro non è disponibile al momento"
    else:
        num_copy = library.get(book_name_lower)
        library[book_name_lower] = num_copy - 1
        if library.get(book_name_lower) == 0:
            library.pop(book_name_lower)
        return True, "La vendita ha avuto successo"


# Funzione che implementa crittografia ROT-13
def critt_rot13(stringa):
    alfa = string.ascii_lowercase
    stringa_lower = stringa.lower()
    cript = ""
    for i, char in enumerate(stringa_lower):
        ind = alfa.index(stringa_lower[i])
        if ind < 13:
            cript += alfa[ind+13]
        else:
            temp = ind - 13
            cript += alfa[temp]
    return cript

# Funzione che implementa crittografia ROT-13 (versione alternativa)
cifrario = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u',
            'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c',
            'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k',
            'y': 'l', 'z': 'm', 'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S',
            'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A',
            'O': 'B', 'P': 'C', 'Q': 'D', 'R': 'E', 'S': 'F', 'T': 'G', 'U': 'H', 'V': 'I',
            'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M'}


def basic_rot(stringa):
    nuova_stringa = ""
    for carattere in stringa:
        if carattere in cifrario:
            nuova_stringa += cifrario[carattere]
        else:
            nuova_stringa += carattere
    return nuova_stringa


# Funzione che calcola il fattoriale di un numero
def fattoriale(num):
    if num == 0:
        return 1
    return num * fattoriale(num-1)


# Funzione  funzione ricorsiva che restituisce in output i numeri della sequenza di Fibonacci,
# entro una soglia specifica impostata dall'utente
def fibonacci(start, soglia, lista):
    if start == 0:
        lista.append(0)
        lista.append(1)
    val = lista[len(lista)-1]+lista[len(lista)-2]
    if start >= soglia:
        return lista
    lista.append(val)
    fibonacci(start+1, soglia, lista)
    return lista


def fibonacci2(n):
    if n <= 1:
        return n
    else:
        return fibonacci2(n - 1) + fibonacci2(n - 2)


# Funzione che restituisce le informazini relative al SO
def get_info_so():
    print("Il Sistema attualmente in uso è: " + platform.system())
    print("Info Release: " + platform.release())


# Funzione che restiutisce il corrispondente codice ascii dato un char
def get_ascii_code(char):
    return ord(char)


# Funzione che restituisce la dimensione della directory di lavoro corrente
def get_folder_size(folder_path):
    size = 0
    for path, dirs, files in os.walk(folder_path):
        #print(path, dirs, files)
        for f in files:
            fp = os.path.join(path, f)
            size += os.path.getsize(fp)
    return size


# Funzione che invia mail tramite gmail
def send_mail(sender, receiver, text):
    smtp_server = "127.0.0.1"
    port = 1025
    server = smtplib.SMTP(smtp_server, port)
    sender_email = sender
    receiver_email = receiver
    message = text
    server.sendmail(sender, receiver, message)
    '''print("""
        Questa è la funzione Postino: spedisce eMail utilizzando Gmail!
        Server: smtp.gmail.com
        Porta: 587
        Si richiedono: Username, Password, Destinatario, Oggetto e Messaggio da inviare.
        """)

    username = "fabio.grs96@gmail.com"
    password = "ciao"
    destinatario = "fabio.grs96@gmail.com"
    oggetto = "prova"
    messaggio = "mail di prova"
    contenuto = f"Subject: {oggetto}\n\n{messaggio}"
    print("Sto effettuando la connessione col Server...")
    email = smtplib.SMTP("smtp.gmail.com", 587)
    email.ehlo()
    email.starttls()
    email.login(username, password)
    print("Sto inviando...")
    email.sendmail(username, destinatario, contenuto)
    email.quit()
    print("Messaggio Inviato!")'''


# Funzione che ricerca tutti i file pdf in un determinato percorso
def search_pdf(path):
    if not os.path.isdir(path):
        print(f"Il percorso inserito '{path}' risulta non essere un percorso idoneo. Verifica e riprova, grazie.\n")
        return None
    contatore = 0
    pdf_list = []
    for cartella, sottocartelle, files in os.walk(path):
        for file in files:
            if file.endswith(".pdf"):
                pdf = os.path.join(cartella, file)
                #print(f"Trovato file pdf: {pdf}\n")
                contatore += 1
                pdf_list.append(pdf)
    return contatore, pdf_list


# Funzione che crea copie di backup di un file
def create_backup(file_path, backup_path):
    if not os.path.isdir(backup_path):
        print(f"Il percorso di backup inserito '{backup_path}' risulta non essere un percorso idoneo. Verifica e riprova, grazie.\n")
        return None
    if not os.path.isfile(file_path):
        print(f"Il percorso del file da copiare '{file_path}' risulta non essere un percorso idoneo. Verifica e riprova, grazie.\n")
        return None
    onlydir = [f for f in os.listdir(backup_path) if os.path.isdir(os.path.join(backup_path, f))]
    #print(onlydir)
    if "Backup" not in onlydir:
        print("la cartella di backup non esiste")
        os.mkdir(os.path.join(backup_path, "Backup"))
        print("cartella di backup creata")
    else:
        print("cartella di backup già esistente")
    complete_backup_path = os.path.join(backup_path, "Backup")
    file_name = os.path.basename(file_path)
    list = file_name.split(".")
    backup_file_name = ""
    for i, elem in enumerate(list):
        if i == 1:
            backup_file_name += "_backup."
        backup_file_name += elem
    complete_path = os.path.join(complete_backup_path, backup_file_name)
    shutil.copyfile(file_path, complete_path)


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

    # Esercizio 7: restituire l'inverso di una stringa
    print(reverser("abcd"))

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

    # Esercizio 8: scrivere una funzione che riconose se una parola è palindroma oppure no
    print(is_palindroma("inani"))
    print(smart_is_palindroma("kayak"))

    # Esercizio 9: implementare la funzione len()
    print(len_list([1, 2, 3]))

    # Esercizio 10: in base ai valori restistuire istogrammi di asterischi
    istogram_generator([3, 5, 7, 9])

    # Esercizio 11: data una lista di stringhe restituire la corrisponde lista contenente le lungheze delle stringhe
    print(len_words(["ciao", "a", "abba", "tre"]))

    # Esercizio 12: Scrivi una funzione a cui passare una stringa come parametro, e che restituisca un dizionario
    # rappresentante la "frequenza di comparsa" di ciscun carattere componente la stringa.
    print(frequenzimetro("aaabcddfgddra"))

    # Esercizio 13: verificare se un valore è presente in una lista e restituiire l'indice
    print(check_elem(4, [1,2,3,4,5]))

    # Esercizio 14: implementare il linguaggio rovarspraket
    #print(rovarspraket("Ciao! questo programma traduce un testo passato in rövarspråket. Ció significa che raddoppia ogni consonante delle parole e ci mette una o in mezzo..."))

    # Esercizio bonus: converte file excel in txt
    #excel_to_txt("db_alimenti.xls")
    # Esercizio bonus: estrae lista similarità da file excel e converte in file txt
    #similarity_list("db_alimenti.xls")

    # Esercizio 15: calcolare area di una forma geometrica scelta dall'utente
    #area = calc_area(answer)
    #print(area)

    '''area = -1
    while area == -1:
        answer = input(
            "Per quale forma serve calcolare l'area? \n - Quadrato \n - Rettangolo \n - Cerchio \n - Triangolo \n")
        area = calc_area(answer)
        print(area)'''

    # Esercizio 16: scrivere funzione che converte una misura in metri in scale differenti
    converter = {
        "iarde": 1,
        "pollici": 2,
        "piedi": 3,
        "miglia": 4
    }

    meters = 4
    measure = 1
    print(convert2(meters))

    # Esercizio 17: scrivere funzione che converte tre valori (giorni, ore, minuti) nel totale in secondi
    days = 3
    hours = 2
    minutes = 59
    print(time_in_seconds(days, hours, minutes))

    # Esercizio 18: generare una password di 8 caratteri casuale
    print(soft_pwd())

    # Esercizio 19: generare indirizzo MAC casuale
    print(gen_MAC())
    print(genera_mac())

    # Esercizio 20: data una parola in input, trovare tutte le altre parole presenti in un elenco che fanno rima
    parola = "casa"
    dizionario = ["ciao", "sgasa", "sa", "invasa", "gatto", "asa"]
    print(rimario(parola, dizionario))

    # Esercizio 21: definire una funzione che verifica se un libro è presente in libreria e conclude 'acquisto
    libreria = {
        "2001: odissea nello spazio": 2,
        "moby dick": 3,
        "i promessi sposi": 1
    }

    '''for i in range(5):
        answer = input("Quale libro desidera? \n")
        result, message = vendi_libri(libreria, answer)
        print(message)
        print("Libri da ordinare: ", order_list)'''

    # Esercizio 22: implementare crittografia ROT-13
    print(critt_rot13("ciao"))
    print(basic_rot("ciao"))

    # Esercizio 23: implementare funzione che calcola il fattoriale di un numero
    fattoriale(5)

    # Esercizio 24: implementare serie di fibonacci (con soglia)
    print(fibonacci(0, 20, []))
    limite=4
    for num in range(1, limite + 1):
        print(fibonacci2(num))

    # Esercizio 25: scrivere funzione che restituisce info riguardo il sistema operativo
    get_info_so()

    # Esercizio 26: scrivere funzione che restituisce il corrispondente codice ascci dato un carattere
    print(get_ascii_code("a"))

    # Esercizio 27: scrivere funzione che restituisce la dimensione della directory di lavoro corrente
    print(get_folder_size(os.getcwd()))

    # Esercizio 28: scrivere funzione che invia mail tramite gmail
    # send_mail("fabio.grs96@gmail.com", "ale.grs96@gmail.com", "Subject: Hi there. This message is sent from Python.")

    # Esercizio 29: La funzione dovrà avere le seguenti caratteristiche:
    #
    #     Il percorso fornito dovrà essere anzitutto validato, in quanto deve portare a una cartella esistente
    #     La funzione dovrà fornire un elenco dei file pdf (con/relativo/percorso) man mano che questi vengono trovati
    #     In fine la funzione dovrà fornire in output il totale dei file .pdf che sono stati trovati durante la
    #     scansione.
    path = "C:/Users/Fabio/Desktop/Utilities"
    # lista, counter = search_pdf(path)
    # print(lista)
    # print(counter)

    lista = [["a","b"], ["c","d"], ["e", "f"]]
    for list1, list2 in lista:
        print(list1, list2)

    # for cartella, sottocartelle, files in os.walk(path):
    #    print(cartella, sottocartelle, files)

    # Esercizio 30: Scrivi una funzione "file_backup" che sia in grado di effettuare copie di backup
    # di determinati tipi di file
    file_path = "C:/Users/Fabio/Desktop/AA_Template libretti formazione_trasversale_NEW.xlsx"
    create_backup(file_path, path)