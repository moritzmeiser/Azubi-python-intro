# To-Do Listen Programm in Python

'''
Ein einfaches To-Do Listen Programm, das dem Benutzer ermöglicht, Aufgaben hinzuzufügen, anzuzeigen und zu löschen.
Das Programm bietet folgende Funktionen:
1. Aufgabe hinzufügen
2. Aufgaben anzeigen
3. Beenden

Implementiere die Funktionen aufgabe_hinzufuegen und aufgaben_anzeigen, die die entsprechenden Aktionen durchführen.
Die Funktion hauptmenue soll das Hauptmenü des Programms darstellen und die Benutzerinteraktion ermöglichen.


'''

def aufgabe_hinzufuegen(todo_liste):
    aufgabe = input("Gib die neue Aufgabe ein: ")
    ## Füge hier die aufgabe der liste hinzu################

    ##############################
    print(f"Aufgabe '{aufgabe}' wurde hinzugefügt.")

def aufgaben_anzeigen(todo_liste):
    if not todo_liste:
        ## Gib eine Nachricht aus, dass die Liste bereits leer ist################

        ##############################
    else:
        print("To-Do Liste:")
        #die Folgende for-schleife gibt die Aufgaben in der Liste aus
        #fülle die {} aus sodass erst der index und dann die aufgabe ausgegeben wird
        for index, aufgabe in enumerate(todo_liste, start=1):
            print(f"{}. {}")


def hauptmenue():
    # Liste für die To-Do Aufgaben
    # todo_list.append("Aufgabe 1") fügt aufgaben hinzu
    # todo_list.pop(0) löscht aufgaben

    todo_liste = []
    while True:
        print("\nTo-Do Listen Programm")
        print("1. Aufgabe hinzufügen")
        print("2. Aufgaben anzeigen")
        print("3. Beenden")

        wahl = input("Gib deine Wahl ein (1/2/3/4): ")

        if wahl == '1':
            aufgabe_hinzufuegen(todo_liste)
        elif wahl == '2':
            aufgaben_anzeigen(todo_liste)
        elif wahl == '3':
            print("Programm beendet.")
            break
        else:
            print("Ungültige Wahl. Bitte wähle eine Option von 1 bis 4.")

if __name__ == "__main__":
    hauptmenue()
