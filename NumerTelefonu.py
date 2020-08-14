import re

moList = []
phoneList = []
phoneRegex1 = re.compile(r'(\(\d\d\d\)\s)?\d\d\s\d\d\s\d\d\d') #(022) 44 32 180
phoneRegex2 = re.compile(r'(\(\d\d\)\s)?\d\d\s\d\d\d\s\d\d') #(22) 44 32 180
phoneRegex3 = re.compile(r'(\d\d)?\d\d\d\d\d\d\d') #224432180
phoneRegex4 = re.compile(r'(\(\d\d\)\s)?\d\d\d\s\d\d\s\d\d') #22 443 21 80
phoneRegex5 = re.compile(r'\+48\d\d\d\d\d\d\d\d\d') #+48720310180
phoneRegex6 = re.compile(r'(\+48\s)?\d\d\d\s\d\d\d\s\d\d\d') #+48 720 310 180
phoneRegex7 = re.compile(r'(0048\s)?\d\d\d\s\d\d\d\s\d\d\d') #0048 720 310 180
phoneRegex8= re.compile(r'0048\d\d\d\d\d\d\d\d\d') #0048720310180
phoneRegex9 = re.compile(r'(\d\d-)?\d\d\d-\d\d-\d\d') #22-443-21-80


print('Witamy w programie "Znajdź polski numer telefonu?"\nWpisz tekst, by sprawdzić, czy zawiera polski numer telefonu\nWpisz "Wyjdź", aby zakończyć...')


def filterNumber(numberList):
        for i in numberList:
                if i is not None:
                        phoneList.append(i)
        

def toNumerTelefonu(numer):
        mo1 = phoneRegex1.search(n)
        mo2 = phoneRegex2.search(n)
        mo3 = phoneRegex3.search(n)
        mo4 = phoneRegex4.search(n)
        mo5 = phoneRegex5.search(n)
        mo6 = phoneRegex6.search(n)
        mo7 = phoneRegex7.search(n)
        mo8 = phoneRegex8.search(n)
        mo9 = phoneRegex9.search(n)
        if mo5 or mo8 is not None:
                moList = [mo1, mo2, mo4, mo5, mo6, mo7, mo8, mo9]
        elif mo6 or mo7 is not None:
                moList = [mo1, mo3, mo4, mo5, mo6, mo7, mo9, mo9]
        else:
                moList = [mo1, mo2, mo3, mo4, mo5, mo6, mo7, mo8, mo9]
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
