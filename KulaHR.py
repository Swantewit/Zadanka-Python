import random

print('Zadaj związane z rekrutacją pytanie')
print('A magiczna kula odpowie Ci na nie...')

while True:
    pytanie = input()
    ans = random.randint(1,20)
    if ans == 1:
        print('Na pewno tak!')
    elif ans == 2:
        print('Myślę, że nie...')
    elif ans == 3:
        print('Zapytaj po obiedzie.')
    elif ans == 4:
        print('Lepiej, żebym teraz nie mówiła...')
    elif ans == 5:
        print('Idź popracować, a ja się namyślę')
    elif ans == 6:
        print('Zatrudnić!')
    elif ans == 7:
        print('Nie zatrudniać!')
    elif ans == 8:
        print('Kłamie w CV!')
    elif ans == 9:
        print('Gwiazdy mówią... Zapytaj inaczej...')
    elif ans == 10:
        print('Fajnie tak decydować o ludzkich losach, co? Przypomnij sobie, jak to było szukać pracy!')
    elif ans == 11:
        print('Podrzuć CV. To które wyląduje jako ostatnie - wygrywa')
    elif ans == 12:
        print('Myślę, że nie...')
    elif ans == 13:
        print('Gwiazdy mówią, że nie...')
    elif ans == 14:
        print('Gwiazdy mówią, że tak')
    elif ans == 15:
        print('Do stu tysięcy źle wymierzonych KPI-ów, może czasem samodzielnie podejmij decyzję?!')
    elif ans == 16:
        print('Umiesz wróżyć z fusów? Ech. Ja też nie.')
    elif ans == 17:
        print('Zapytaj jutro')
    elif ans == 18:
        print('Przejrzyj jeszcze raz wybrane CV. Wierzę w Ciebie!')
    elif ans == 19:
        print('Zapytaj przełożonego, nie magicznej kuli. Zaufaj mi.')
    elif ans == 20:
        print('Hm... To trudne pytanie.')
    
