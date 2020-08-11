import re

moList = []
phoneList = []
phoneRegex = [re.compile(r'(\(\d\d\d\)\s)?\d\d\s\d\d\s\d\d\d')
,re.compile(r'(\(\d\d\)\s)?\d\d\s\d\d\d\s\d\d')
,re.compile(r'(\d\d)?\d\d\d\d\d\d\d')
,re.compile(r'(\(\d\d\)\s)?\d\d\d\s\d\d\s\d\d')
,re.compile(r'(0048\s)?\d\d\d\s\d\d\d\s\d\d\d')
,re.compile(r'(\d\d\s-\s)?\d\d\d\s-\s\d\d\s-\s\d\d')
,re.compile(r'(\d\d-)?\d\d\d-\d\d-\d\d')
,re.compile(r'\d\d\d-\d\d-\d\d')
,re.compile(r'(\+48\s)?\d\d\d\s\d\d\d\s\d\d\d')
,re.compile(r'0048\d\d\d\d\d\d\d\d\d')
,re.compile(r'\+48\d\d\d\d\d\d\d\d\d')]


print('Witamy w programie "Znajdź polski numer telefonu?"\nWpisz tekst, by sprawdzić, czy zawiera polski numer telefonu\nWpisz "Wyjdź", aby zakończyć...')


def filterNumber(numberList):
        for i in numberList:
                if i is not None:
                        phoneList.append(i)
        

def toNumerTelefonu(numer):
        for i in phoneRegex:
            moList.append(i.search(numer))
        filterNumber(moList)
        for i in phoneList:
                print('Znaleziono numer telefonu: ' + i.group())


while True:
    n = input()

    if n == 'Wyjdź':
            print('Dziękujemy za skorzystanie z programu.')
            break
    else:
        toNumerTelefonu(n)
