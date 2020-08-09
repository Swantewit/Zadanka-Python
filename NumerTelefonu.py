import re

moList = []
phoneList = []
phoneNumRegex1 = re.compile(r'\(\d\d\d\)\s\d\d\s\d\d\s\d\d\d')
phoneNumRegex2 = re.compile(r'\(\d\d\)\s\d\d\s\d\d\d\s\d\d')
phoneNumRegex3 = re.compile(r'\d\d\d\d\d\d\d\d\d')
phoneNumRegex4 = re.compile(r'\d\d\d\d\d\d\d')
phoneNumRegex5 = re.compile(r'0048 \d\d\d \d\d\d \d\d\d')
phoneNumRegex6 = re.compile(r'\d\d\s-\s\d\d\d\s-\s\d\d\s-\s\d\d')
phoneNumRegex7 = re.compile(r'\d\d\d\s-\s\d\d\s-\s\d\d')
phoneNumRegex8 = re.compile(r'\d\d-\d\d\d-\d\d-\d\d')
phoneNumRegex9 = re.compile(r'\d\d\d-\d\d-\d\d')
phoneNumRegex10 = re.compile(r'\+48\s\d\d\d\s\d\d\d\s\d\d\d')
phoneNumRegex11 = re.compile(r'0048\d\d\d\d\d\d\d\d\d')
phoneNumRegex12 = re.compile(r'\+48\d\d\d\d\d\d\d\d\d')
phoneNumRegex13 = re.compile(r'\d\d\d\s\d\d\s\d\d')

print('Witamy w programie "Znajdź polski numer telefonu?"\nWpisz tekst, by sprawdzić, czy zawiera polski numer telefonu\nWpisz "Wyjdź", aby zakończyć...')


def filterNumber(numberList):
        for i in numberList:
                if i is not None:
                        phoneList.append(i)
        

def toNumerTelefonu(numer):
        mo1 = phoneNumRegex1.search(n)
        mo2 = phoneNumRegex2.search(n)
        mo3 = phoneNumRegex3.search(n)
        mo4 = phoneNumRegex4.search(n)
        mo5 = phoneNumRegex5.search(n)
        mo6 = phoneNumRegex6.search(n)
        mo7 = phoneNumRegex7.search(n)
        mo8 = phoneNumRegex8.search(n)
        mo9 = phoneNumRegex9.search(n)
        mo10 = phoneNumRegex10.search(n)
        mo11 = phoneNumRegex11.search(n)
        mo12 = phoneNumRegex12.search(n)
        mo13 = phoneNumRegex13.search(n)
        moList.extend([mo1, mo2, mo3, mo4, mo5, mo6, mo7, mo8, mo9, mo10, mo11, mo12, mo13])
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
