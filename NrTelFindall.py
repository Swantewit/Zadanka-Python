import re

moList = []
phoneList = []
phoneRegex1 = re.compile(r'\(\d\d\d\)\s\d\d\s\d\d\s\d\d\d') #(022) 44 32 180
phoneRegex2 = re.compile(r'\(\d\d\)\s\d\d\s\d\d\d\s\d\d') #(22) 44 32 180
phoneRegex3 = re.compile(r'\d\d\d\d\d\d\d') #4432180
phoneRegex4 = re.compile(r'\(\d\d\)\s\d\d\d\s\d\d\s\d\d') #(22) 443 21 80
phoneRegex5 = re.compile(r'\+48\d\d\d\d\d\d\d\d\d') #+48720310180
phoneRegex6 = re.compile(r'\+48\s\d\d\d\s\d\d\d\s\d\d\d') #+48 720 310 180
phoneRegex7 = re.compile(r'0048\s\d\d\d\s\d\d\d\s\d\d\d') #0048 720 310 180
phoneRegex8= re.compile(r'0048\d\d\d\d\d\d\d\d\d') #0048720310180
phoneRegex9 = re.compile(r'\d\d-\d\d\d-\d\d-\d\d') #22-443-21-80
phoneRegex10 = re.compile(r'\d\d\d\s\d\d\s\d\d') #443 21 80
phoneRegex11 = re.compile(r'\d\d\d-\d\d-\d\d') #443-21-80
phoneRegex12 = re.compile(r'\d\d\s\d\d\d\s\d\d\s\d\d') #22 443 21 80


print('Witamy w programie "Znajdź polski numer telefonu?"\nWpisz tekst, by sprawdzić, czy zawiera polski numer telefonu\nWpisz "Wyjdź", aby zakończyć...')


def filterNumber(numberList):
        for i in numberList:
                if i != []:
                        phoneList.append(i)
        

def toNumerTelefonu(numer):
        mo1 = phoneRegex1.findall(n)
        mo2 = phoneRegex2.findall(n)
        mo3 = phoneRegex3.findall(n)
        mo4 = phoneRegex4.findall(n)
        mo5 = phoneRegex5.findall(n)
        mo6 = phoneRegex6.findall(n)
        mo7 = phoneRegex7.findall(n)
        mo8 = phoneRegex8.findall(n)
        mo9 = phoneRegex9.findall(n)
        mo10 = phoneRegex10.findall(n)
        mo11 = phoneRegex11.findall(n)
        mo12 = phoneRegex12.findall(n)
        if mo5 or mo8 is not None:
                moList = [mo1, mo2, mo4, mo5, mo6, mo7, mo8, mo9, mo10, mo11, mo12]
        elif mo6 or mo7 is not None:
                moList = [mo1, mo3, mo4, mo5, mo6, mo7, mo9, mo9, mo10, mo11, mo12]
        else:
                moList = [mo1, mo2, mo3, mo4, mo5, mo6, mo7, mo8, mo9, mo10, mo11, mo12]
        filterNumber(moList)
        print('Znaleziono następujące numery' + str(phoneList))
        

while True:
    n = input()

    if n == 'Wyjdź':
            print('Dziękujemy za skorzystanie z programu.')
            break
    else:
        toNumerTelefonu(n)
