import random
import sys

print("""
V tomto programe dojde k prikladu pre hadzanie kockami v TTRPG Dungeons & Dragons.
Pre kazde hodenie musi pouzivatel zadat toto ako 2d6.
Pri tomto je pre cislo pocet hodenych kociek a cislo za d predstavuje pocet stien na kocke.
Pre ukoncenie hrac napise QUIT""")

#hlavy loop
while True:
    try:
        print()
        diceStr = input("-> ") #zadanie kociek
        if diceStr.upper() == 'QUIT':
            print("Dakujem za pouzitie.")
            sys.exit()

        #vycustenie stringu
        diceStr = diceStr.lower().replace(" ", " ")

        #vyhladanie "d" v stringu vstupu:
        dIndex = diceStr.find('d')
        if dIndex == -1:
            raise Exeption('Chybajuce "d" znak.')

        #ziskanie poctu kociek (2 v 2d6)
        pocetKociek = diceStr[:dIndex]
        if not pocetKociek.isdecimal():
            raise Exception("Chybajuci pocet kociek.")
        pocetKociek = int(pocetKociek)

        #najdenie znamienka + alebo - v znaku
        modIndex = diceStr.find('+')
        if modIndex == -1:
            modIndex = diceStr.find('-')

        #najdi pocet stien kocky (6 v 2d6+1)
        if modIndex == -1:
            pocetStien = diceStr[dIndex + 1 :]
        else:
            pocetStien = diceStr[dIndex + 1 : modIndex]
        if not pocetStien.isdecimal():
            raise Exception('Chybajuci pocet stien.')
        pocetStien = int(pocetStien)

        #najdi bonus ku hodu (1 v 2d6+1)
        if modIndex == -1:
            modAmount = 0
        else:
            modAmount = int(diceStr[modIndex + 1 :])
            if diceStr[modIndex] == '-':
                #zmena bonnusu na negativny
                modAmount = -modAmount

        #simulovanie hodu:
        rolls = []
        for i in range(pocetKociek):
            rollVysledook = random.randint(1, pocetStien)
            rolls.append(rollVysledook)

        #Ukaz celkovy vysledok
        print('Celkovy vysledok: ', sum(rolls) + modAmount, 'Kazda kocka: ' , end = '')

        #zobraz jednotlive hody
        for i, roll in enumerate(rolls):
            rolls[i] = str(roll)
        print(', '.join(rolls), end = '')

        #zobraz modifikovane mnzstvo
        if modAmount != 0:
            modSign = diceStr[modIndex]
            print(', {}{}'.format(modSign, abs(modAmount)), end='')



    except Exception as exc:
            #chyt akukovek zobrazenu spravu pre pouzivatela
            print("Neplatny vstup. Zadaj nieco ako '2d6' alebo '1d20+5'")
            print('Vstup bol nespravny preto lebo: '+str(exc))
            continue #chod nazad k hadzaniu kockou

