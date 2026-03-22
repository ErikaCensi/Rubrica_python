import json

# Chiedi input
def chiedi_input(messaggio):
    while True:
        variabile = input(messaggio)
        if variabile.strip():
            return variabile.strip().title()
        print("Inserimento non valido.")

# Aggiungi contatto
def aggiungi_contatto(rubrica):
        nome = chiedi_input("Inserisci nome: ")
        numero = chiedi_input("Inserisci numero di telefono: ")
        if nome in rubrica:
            print("Contatto già esistente.")
        else:
            rubrica[nome] = numero
            print("Contatto aggiunto!")

# Ordinamento rubrica
def ordina(rubrica):
    for nome, numero in sorted(rubrica.items()):
        print(f"Nome: {nome} | Numero: {numero}")

# Mostra rubrica
def mostra_rubrica(rubrica):
    if not rubrica:
        print("Non ci sono contatti nella tua rubrica.")
    else:
        ordina(rubrica)

# Trova contatto
def trova_contatto(rubrica):
    contatto = chiedi_input("Chi vuoi cercare? inserisci nome: ")
    if contatto in rubrica:
        print(f"Il numero di {contatto} è : {rubrica[contatto]}")
    else:
        print("Contatto non trovato.")

# Cancella contatto
def cancella_contatto(rubrica):
    contatto = chiedi_input("Di chi vuoi cancellare il numero? Inserisci nome: ")
    if contatto in rubrica:
        rubrica.pop(contatto)
        print("Contatto cancellato!")
    else:
        print("Contatto non trovato.")

# Salva json
def salva_json(rubrica):
    with open ("rubrica.json", "w") as file:
        json.dump(rubrica, file, indent = 4)
        print("Salvataggio eseguito!")

# Leggi json
def leggi_json():
    try:
        with open ("rubrica.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Rubrica
def main():
    rubrica = leggi_json()
    funzioni = {"1" : aggiungi_contatto, "2" : mostra_rubrica, "3" : trova_contatto, "4" : cancella_contatto}
    print("Ciao, sono la tua rubrica.")
    while True:
        scelta = input("1. Aggiungi contatto\n"
                   "2. Mostra rubrica\n"
                   "3. Trova contatto\n"
                   "4. Cancella contatto\n"
                   "5. Chiudi\n"
                   "Scegli il numero corrispondente: ")
        if scelta == "5":
            break
        if scelta in funzioni:
            funzioni[scelta](rubrica)
        else:
            print("Scelta non valida.")
    salva_json(rubrica)

if __name__ == "__main__":
    main()
