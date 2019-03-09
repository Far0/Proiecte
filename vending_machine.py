import os
import getpass
Portofel = Bani_introdusi = nr = 0
fuck = []
detinut = []
magazin = ['Pepsi', 'Lipton', 'Coca-Cola', 'Fanta',
           'Sprite', 'Gatorade', 'Sandvis', 'Biscuiti', 'Pizza']
preturi = [3, 2, 3, 3, 2, 5, 5, 3, 20]
numar = []
os.system('cls')
os.system('color B')
print('Bine ai venit la vending machine-ul nostru!')
while True:
    print('\n\nSuma disponibila:',
          Portofel, 'RON\n\nCe doresti sa faci?\n\n1.Adauga\n2.Cumpara\n3.Obiecte cumparate\n4.Adauga obiecte[ADMIN ONLY]\n5.Iesi\n\n')
    optiune = int(input('Ce optiune alegi?\nRaspuns:'))
    os.system('cls')
    if optiune == 1:
        while Bani_introdusi == 0:
            print('Se asteapta bacnota...\n')
            Bani_introdusi = int(input(''))

            if 0 >= Bani_introdusi:
                print('\n\nIntroduce o suma validă\n\n')
                Bani_introdusi = 0
            else:
                os.system('cls')
                Portofel += Bani_introdusi
                print('Tocmai ai introdus', Bani_introdusi, 'RON')
                print('Ai in total', Portofel, 'RON')
                adaugare = int(
                    input('Doresti sa mai adaugi?\n 1.Da\n 2.Nu\nRaspuns:'))
                Bani_introdusi = 0
                if adaugare != 1:
                    os.system('cls')
                    break
    elif optiune == 2:
        for x in range(len(preturi)):
            if len(fuck) != len(preturi):
                nr = nr+1
                fuck.append(int(nr))
                print(str(nr)+'.', magazin[x], preturi[x], 'RON')
            else:
                print(str(fuck[x])+'.', magazin[x], preturi[x], 'RON')
            if x == len(preturi)-1:
                    primesc = int(input('Ce doresti sa cumperi?\nRaspuns:'))
                    if primesc>len(preturi):
                        os.system('cls')
                        print('Nu exista.')
                    else:
                        if Portofel>=preturi[primesc-1]:
                            os.system('cls')
                            print('Ai cumparat',magazin[primesc-1])
                            Portofel= Portofel-preturi[primesc-1]
                            detinut.append(magazin[primesc-1])
                        else:
                            print('Nu ai suficienti bani!')

    elif optiune == 3:
        if len(detinut)==0:
            print('Momentan nu ai cumparat nimic.')
        else:
            print('Momentan ai:')
            for x in range(len(detinut)):
                print('1x',detinut[x])
    elif optiune == 4:
        parola= getpass.getpass(prompt="Parola: ",stream=None)
        if parola == "test":
            shop_nume = input("Ce doresti sa adaugi?\nRaspuns:")
            print('Ce preti vrei sa aibe \"',shop_nume,'\"?')
            shop_pret = int(input('Raspuns:'))
            magazin.append(shop_nume)
            preturi.append(shop_pret)
        else:
            print("Parola gresita")

    else:
        print('La revedere!\nNu uita restul de bani!\nRest:', Portofel, 'RON')
        break
