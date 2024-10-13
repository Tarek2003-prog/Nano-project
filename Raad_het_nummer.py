import random
def play():
    #De naam van de gebruiker vragen
    Gebruikers_naam = str(input('Wat is je naam? '))
    #intro
    print (f'Beste {Gebruikers_naam} in dit spel moet je het getal raden. Het maximum getal mag je zelf kiezen. De aantal pogingen mag je ook zelf kiezen.')
    print ('Succes :)')
    #Ik geef de vrijheid voor de gebruiker om zelf het getl en de pogingen te geven..
    max_getal = int(input(f'{Gebruikers_naam} kies het maximum getal waaruit geraden moet worden: '))
    pogingen = int(input('In hoeveel keer wil je raden?: '))
    willekeurige_getal = random.randint(1, max_getal)
    print (f'Raad een getal tussen 1 en {max_getal} ')
    print (f'Je hebt {pogingen} pogingen om het juiste getal te raden ')
    #for loop
    for poging in range(1, pogingen + 1):
        gok =  int(input(f'Poging {poging} van {pogingen} wat is je gok? '))
    #Als de gebruiker het juiste getal kiest:
        if gok == willekeurige_getal:
            print(f'{Gebruikers_naam} Gefeliciteerd! Je hebt het juiste getal {willekeurige_getal} geraden in {poging} pogingen ')
            break
    #Zo help ik de gebruiker om het getal sneller te vinden.
        elif gok < willekeurige_getal:
            print('Het getal is hoger. ')
        else:
            print ('Het getal is lager ')
    #Als de gebruiker geen pogingen meer heeft:
        if poging == pogingen:
            print (f'Je hebt helaas geen pogingen meer, het juiste getal is {willekeurige_getal}' )
