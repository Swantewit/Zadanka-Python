import random

print('Zadaj związane z rekrutacją pytanie')
print('A magiczna kula odpowie Ci na nie...')

while True:
    pytanie = input()
    ans = ['Na pewno tak!',
    'Myślę, że nie...',
    'Zapytaj po obiedzie.',
    'Lepiej, żebym teraz nie mówiła...',
    'Idź popracować, a ja się namyślę',
    'Zatrudnić!',
    'Nie zatrudniać!',
    'Kłamie w CV!',
    'Gwiazdy mówią... Zapytaj inaczej...',
    'Fajnie tak decydować o ludzkich losach, co? Przypomnij sobie, jak to było szukać pracy!',
    'Podrzuć CV. To które wyląduje jako ostatnie - wygrywa',
    'Myślę, że nie...',
    'Gwiazdy mówią, że nie...',
    'Gwiazdy mówią, że tak',
    'Do stu tysięcy źle wymierzonych KPI-ów, może czasem samodzielnie podejmij decyzję?!',
    'Umiesz wróżyć z fusów? Ech. Ja też nie.',
    'Zapytaj jutro',
    'Przejrzyj jeszcze raz wybrane CV. Wierzę w Ciebie!',
    'Zapytaj przełożonego, nie magicznej kuli. Zaufaj mi.',
    'Hm... To trudne pytanie.']

    print(ans[random.randint(0,len(ans)-1)])
