### Python easy calculator ###
Kwadraten = []

while True:
    kwadratischeInvoer = int(input("Vul hier uw invoer in om te kwadrateren"))
    Gekwadrateerd = kwadratischeInvoer**2
    Kwadraten.append(Gekwadrateerd)
    print(Gekwadrateerd)
    Geschiedenis = input("Type geschiedenis voor de oude antwoorden ")
    
    if Geschiedenis == "geschiedenis":
        print(Kwadraten)