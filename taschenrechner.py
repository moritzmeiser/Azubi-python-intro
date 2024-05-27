# Taschenrechner in Python
'''
Ein Taschenrechner-Programm, das die vier Grundrechenarten Addition, Subtraktion, Multiplikation und Division unterstützt.
Das Programm soll den Benutzer auffordern, eine der vier Operationen auszuwählen und dann zwei Zahlen einzugeben, auf die die Operation angewendet wird.
Das Ergebnis der Berechnung wird dann ausgegeben.

Implementiere die vier Funktionen addieren, subtrahieren und  multiplizieren, die zwei Zahlen als Parameter erhalten und das Ergebnis der jeweiligen Operation zurückgeben.
'''
def addieren(x, y):
    return 

def subtrahieren(x, y):
    return 

def multiplizieren(x, y):
    return 



def main():
    print("Wähle die Operation:")
    print("1. Addition")
    print("2. Subtraktion")
    print("3. Multiplikation")


    while True:
        # Eingabe der Benutzerwahl
        wahl = input("Gib deine Wahl ein (1/2/3/4): ")

        # Prüfen ob die Wahl gültig ist
        if wahl in ['1', '2', '3', '4']:
            zahl1 = float(input("Gib die erste Zahl ein: "))
            zahl2 = float(input("Gib die zweite Zahl ein: "))

            if wahl == '1':
                print(f"{zahl1} + {zahl2} = {addieren(zahl1, zahl2)}")

            elif wahl == '2':
                print(f"{zahl1} - {zahl2} = {subtrahieren(zahl1, zahl2)}")

            elif wahl == '3':
                print(f"{zahl1} * {zahl2} = {multiplizieren(zahl1, zahl2)}")

            
            # Frage den Benutzer, ob er eine weitere Berechnung durchführen möchte
            weitere_berechnung = input("Möchtest du eine weitere Berechnung durchführen? (ja/nein): ")
            if weitere_berechnung.lower() != 'ja':
                break
        else:
            print("Ungültige Eingabe. Bitte wähle eine Option von 1 bis 3.")

if __name__ == "__main__":
    main()
