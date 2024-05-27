

'''
Ein Zahlen-ratespiel, bei dem der Benutzer eine Zahl zwischen 1 und 100 erraten muss.
Das Spiel wurde nicht ganz fertig programmiert. 
Ergänze den fehlenden Teil, um die Bedingung für den Fall zu prüfen, wenn der Tipp zu hoch ist.
Ergänze den fehlenden Teil, um eine Nachricht auszugeben, wenn der Benutzer die Zahl erraten hat.(Zeile 35 ff.)
'''

import random

def zahlenraten():
    #in der Variable Nummer wird eine zufällige Zahl zwischen 1 und 100 gespeichert
    #in der Variable Versuche wird die Anzahl der Versuche gespeichert(am Anfang also 0)
    nummer = random.randint(1, 100)
    versuche = 0

    print("Willkommen zum Zahlenraten-Spiel!")
    print("Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht. Kannst du sie erraten?")

    #Die while-Schleife läuft solange, bis der Benutzer die richtige Zahl erraten hat
    while True:
        tipp = input("Gib deinen Tipp ein: ")

        try:
            #Der angegebene Tipp wird in der Variable Tipp gespeichert
            #Die Anzahl der Versuche wird um 1 erhöht
            tipp = int(tipp)
            versuche += 1

            if tipp < nummer:
                print("Zu niedrig! Versuch es nochmal.")
            # Ergänze den fehlenden Teil hier, um die Bedingung für den Fall zu prüfen, wenn der Tipp zu hoch ist.
            else:
                if 
                    print("Zu hoch! Versuch es nochmal.")
                    
                else:
                    print()#gib eine Nachricht aus, wenn der Benutzer die Zahl erraten hat  
                    break
        except ValueError:
            print("Bitte gib eine gültige Zahl ein.")

if __name__ == "__main__":
    zahlenraten()
