import Raad_het_nummer
import Galgje

def quickfun():
    print('1. Raad het nummer ')
    print('2. Galgje')

    keuze = input('Welke spelletje wilt u spelen? 1. Raad het nummer of 2. Galgje? Kies 1/2: ')
    print(f'Je keuze: {keuze}')

    if keuze == '1':
        print("Start Raad het nummer...")
        Raad_het_nummer.play()  # Zorg ervoor dat play() iets uitvoert
    elif keuze == '2':
        print("Start Galgje...")
        Galgje.play()  # Zorg ervoor dat play() iets uitvoert
    else:
        print("Ongeldige keuze. Kies alstublieft 1 of 2.")

if __name__ == "__main__":
    quickfun()
