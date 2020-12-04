### Python easy calculator ###
Uitkomsten = []

while True:
    InvoerBerekening = input("Wat wilt u berekenen (optellen, aftrekken, delen, vermenigvuldigen of kwadrateren: ")

    if InvoerBerekening == "optellen":
        Getal1, Getal2 = input("Vul hier uw twee getallen in om bij elkaar op te tellen: ").split()
        OptelBerekening = int(Getal1) + int(Getal2)
        Uitkomsten.append(OptelBerekening)
        print(OptelBerekening)

    elif InvoerBerekening == "aftrekken":
        Getal1, Getal2 = input("Vul hier uw twee getallen in om van elkaar af te trekken: ").split()
        AftrekBerekening = int(Getal1) - int(Getal2)
        Uitkomsten.append(AftrekBerekening)
        print(AftrekBerekening)

    elif InvoerBerekening == "delen":
        Getal1, Getal2 = input("Vul hier uw twee getallen in met elkaar te delen: ").split()
        DeelBerekening = int(Getal1) / int(Getal2)
        Uitkomsten.append(DeelBerekening)
        print(DeelBerekening)

    elif InvoerBerekening == "vermenigvuldigen":
        Getal1, Getal2 = input("Vul hier uw twee getallen in met te vermenigvuldigen: ").split()
        VermenigvuldigBerekening = int(Getal1) * int(Getal2)
        Uitkomsten.append(VermenigvuldigBerekening)
        print(VermenigvuldigBerekening)

    elif InvoerBerekening == "kwadrateren":
        Getal1 = int(input("Vul hier uw getal te kwadrateren: "))
        KwadraatBerekening = Getal1**2
        Uitkomsten.append(KwadraatBerekening)
        print(KwadraatBerekening)

    Geschiedenis = input("Type eventueel geschiedenis voor de oude antwoorden: ")
    
    if Geschiedenis == "geschiedenis":
        print(Uitkomsten)