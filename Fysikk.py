import numpy as np

#Definerer tyngdekrefter på forskjellige planeter med dictionary
tyngdekrefter = {
    "Jorden": 9.81,
    "Månen": 1.62,
    "Merkur": 3.7,
    "Venus": 8.87,
    "Mars": 3.71,
    "Jupiter": 24.79,
    "Saturn": 10.44,
    "Uranus": 8.87,
    "Neptun": 11.15,
    "Pluto": 0.26,
    
    9.81: "Jorden",
    1.62: "Månen",
    3.7: "Merkur",
    8.87: "Venus",
    3.71: "Mars",
    24.79: "Jupiter",
    10.44: "Saturn",
    8.87: "Uranus",
    11.15: "Neptun",
    0.26: "Pluto"
    }

#Definerer formlene
def fart(strekning, tid):
    return strekning/tid

def akselrasjon(startfart, sluttfart, tid):
    return (sluttfart-startfart)/tid

def tyngde(masse, planet):
    return masse*tyngdekrefter[planet]

def kraft(masse, startfart, sluttfart, tid):
    return akselrasjon(startfart, sluttfart, tid)*masse

def kraft_masse_akselrasjon(masse, akselrasjon):
    return masse*akselrasjon

def arbeid(masse, startfart, sluttfart, tid, strekning):
    return kraft(masse, akselrasjon(startfart, sluttfart, tid))*strekning

def arbeid_masse_akselrasjon_strekning(masse, akselrasjon, strekning):
    return kraft_masse_akselrasjon(masse, akselrasjon)*strekning

def arbeid_kraft_strekning(kraft, strekning):
    return kraft*strekning

def effekt(masse, startfart, sluttfart, tid, strekning, tid2):
    return arbeid(masse, akselrasjon(startfart, sluttfart, tid), strekning)/tid2

def effekt_masse_akselrasjon_strekning_tid(masse, akselrasjon, strekning, tid):
    return (masse*akselrasjon*strekning)/tid

def effekt_kraft_strekning_tid(kraft, strekning, tid):
    return (kraft*strekning)/tid

def effekt_arbeid_tid(arbeid, tid):
    return arbeid/tid





def strekning_fart_tid(fart, tid):
    return tid*fart

def tid_strekning_fart(strekning, fart):
    return strekning/fart


def startfart_akselrasjon_tid_sluttfart(akselrasjon, tid, sluttfart):
    return -(akselrasjon*tid) + sluttfart

def sluttfart_akselrasjon_tid_startfart(akselrasjon, tid, startfart):
    return akselrasjon*tid + startfart

def tid_sluttfart_startfart_akselrasjon(sluttfart, startfart, akselrasjon):
    return (sluttfart-startfart)/akselrasjon


def planet_tyngde_masse(tyngde, masse):
    return(tyngdekrefter[tyngde/masse])

def masse_tyngde_planet(tyngde, planet):
    return tyngde/(tyngdekrefter[planet])


def akselrasjon_kraft_masse(kraft, masse):
    return kraft/masse

def masse_kraft_akselrasjon(kraft, akselrasjon):
    return kraft/akselrasjon


def strekning_arbeid_kraft(arbeid, kraft):
    return arbeid/kraft

def kraft_arbeid_strekning(arbeid, strekning):
    return arbeid/strekning


def arbeid_effekt_tid(effekt, tid):    return effekt*tid

def tid_arbeid_effekt(arbeid, effekt):
    return arbeid/effekt

#Definerer inputer
def strekning_input():
    strekning = float(input("Hva er strekningen i meter? "))

def tid_input():
    tid1 = float(input("Hva er tiden i sekunder? "))

def tid2_input():
    tid = float(input("Hva er den andre tiden i sekunder? "))

def fart_input():
    fart = float(input("Hva er farten i m/s? "))

def akselrasjon_input():
    akselrasjon = float(input("Hva er akselrasjonen i m/s^2? "))

def startfart_input():
    startfart = float(input("Hva er startfarten i m/s ? "))

def sluttfart_input():
    sluttfart = float(input("Hva er sluttfarten i m/s ? "))

def masse_input():
    masse = float(input("Hva er massen i kilogram? "))

def planet_input():
    planet = float(input("Hvilken planet gjelder tyngdekraften for? "))

def kraft_input():
    kraft = float(input("Hvor stor er kraften i Newton? "))

def tyngde_input():
    kraft = float(input("Hvor stor er tyngden i Newton? "))

def arbeid_input():
    arbeid = float(input("Hva er mengden arbeid i Newtonmeter eller Joule? "))

def effekt_input():
    effekt = float(input("Hva er effekten i watt? "))

#Selve utregningen og input
funksjon = float(input('''Hvilken funksjon vil du bruke?
1 = finne fart med strekning og tid
2 = finne akselrasjon med startfart, sluttfart og tid
3 = finne tyngde med masse og planet
4 = finne kraft med masse, startfart, sluttfart og tid
5 = finne kraft med masse og akselrasjon
6 = finne arbeid med masse, startfart, sluttfart, tid og strekning
7 = finne arbeid med masse, akselrasjon og strekning
8 = finne arbeid med kraft og strekning
9 = finne effekt med masse, startfart, sluttfart, tid, strekning og tid
10 = finne effekt med masse, akselrasjon, strekning og tid
11 = finne effekt med kraft, strekning og tid
12 = finne effekt med arbeid og tid

Vei-fart-tid
13 = finne strekning med fart og tid
14 = finne tid med strekning og fart

Akselrasjon
15 = finne startfart med akselrasjon, tid og sluttfart
16 = finne sluttfart med akselrasjon, tid og startfart
17 = finne tid med sluttfart, startfart og akselrasjon

Tyngde
18 = finne planet med tyngde og masse
19 = finne masse med tyngde og planet

Kraft
20 = finne akselrasjon med kraft og masse
21 = finne masse med kraft og akselrasjon

Arbeid
22 = finne strekning med arbeid og kraft
23 = finne kraft med arbeid og strekning

Effekt
24 = finne arbeid med effekt og tid
25 = finne tid med arbeid og effekt
'''))
print()

if funksjon == 1:
    print("Fart = strekning/tid\n")
    
    strekning_input()
    tid_input()
    svar = fart(strekning, tid)


elif funksjon == 2:
    print("Akselrasjon = (startfart - sluttfart)/tid\n")
    
    startfart_input()
    sluttfart_input()
    tid_input()
    svar = akselrasjon(startfart, sluttfart, tid)


elif funksjon == 3:
    print("Tyngde = masse*gravitasjon\n")
    
    masse_input()
    planet_input()
    svar = tyngde(masse, planet)


elif funksjon == 4:
    print("Kraft = masse*akselrasjon")
    print("Akselrasjon = (startfart - sluttfart)/tid")
    print()
    print("Kraft = masse*((startfart - sluttfart)/tid)\n")
    
    masse_input()
    startfart_input()
    sluttfart_input()
    tid_input()
    svar = kraft(masse, startfart, sluttfart, tid)

elif funksjon == 5:
    print("Kraft = masse*akselrasjon\n")
    
    masse_input()
    akselrasjon_input()
    svar = kraft_masse_akselrasjon()

elif funksjon == 6:
    print("Arbeid = kraft*strekning")
    print("Kraft = masse*akselrasjon")
    print("Akselrasjon = (startfart - sluttfart)/tid")
    print()
    print("Arbeid = masse*((startfart - sluttfart)/tid)*strekning\n")
    
    masse_input()
    startfart_input()
    sluttfart_input()
    tid_input()
    strekning_input()
    svar = arbeid(masse, startfart, sluttfart, tid, strekning)

elif funksjon == 7:
    print("Arbeid = kraft*strekning")
    print("Kraft = masse*akselrasjon")
    print()
    print("Arbeid = masse*akselrasjon*strekning\n")

    masse_input()
    akselrasjon_input()
    strekning_input()
    svar = arbeid_masse_akselrasjon_strekning(masse, akselrasjon, strekning)

elif funksjon == 8:
    print("Arbeid = kraft*strekning")
    kraft_input()
    strekning_input()
    svar = arbeid_kraft_strekning(kraft, strekning)

elif funksjon == 9:
    print("Effekt = arbeid/tid")
    print("Arbeid = kraft*strekning")
    print("Kraft = masse*akselrasjon")
    print("Akselrasjon = (startfart - sluttfart)/tid")
    print()
    print("Effekt = (masse*((startfart - sluttfart)/tid)*strekning)/tid\n")
    
    masse_input()
    startfart_input()
    sluttfart_input()
    tid_input()
    strekning_input()
    tid2_input()
    svar = effekt(masse, startfart, sluttfart, tid, strekning, tid2)

elif funksjon == 10:
    print("Effekt = arbeid/tid")
    print("Arbeid = kraft*strekning")
    print("Kraft = masse*akselrasjon")
    print()
    print("Effekt = (masse*akselrasjon*strekning)/tid\n")

    masse_input()
    akselrasjon_input()
    strekning_input()
    tid_input()
    svar = effekt_masse_akselrasjon_strekning_tid(masse, akselrasjon, strekning, tid)

elif funksjon == 11:
    print("Effekt = arbeid/tid")
    print("Arbeid = kraft*strekning")
    print()
    print("Effekt = (kraft*strekning)/tid\n")

    kraft_input()
    strekning_input()
    tid_input()
    svar = effekt_kraft_strekning_tid(kraft, strekning, tid)

elif funksjon == 12:
    print("Effekt = arbeid/tid\n")

    arbeid_input()
    tid_input()
    svar = effekt_arbeid_tid(arbeid, tid)
    
elif funksjon == 13:
    print("Strekning = fart*tid\n")
    
    fart_input()
    tid_input()
    svar = strekning_fart_tid(fart, tid)

elif funksjon == 14:
    print("Tid = strekning/fart\n")
    
    strekning_input()
    fart_input()
    svar = tid_strekning_fart(strekning, fart)

elif funksjon == 15:
    print("Startfart = -(akselrasjon*tid) + sluttfart\n")
    
    akselrasjon_input()
    tid_input()
    sluttfart_input()
    svar = startfart_akserasjon_tid_sluttfart(akselrasjon, tid, sluttfart)

elif funksjon == 16:
    print("Sluttfart = akselrasjon*tid + startfart\n")
    
    akselrasjon_input()
    tid_input()
    startfart_input()
    svar = sluttfart_akselrasjon_tid_startfart(akselrasjon, tid, startfart)

elif funksjon == 17:
    print("Tid = (sluttfart-startfart)/akselrasjon\n")

    sluttfart()
    startfart_input()
    akserasjon_input()
    svar = tid_sluttfart_startfart_akselrasjon(sluttfart, startfart, akselrasjon)

elif funksjon == 18:
    print("Gravitasjon = tyngde/masse\n")

    tyngde_input()
    masse_input()
    svar = planet_tyngde_masse(tyngde, masse)

elif funksjon == 19:
    print("Masse = tyngde/tyngdekrefter\n")

    tyngde_input()
    planet_input()
    svar = masse_tyngde_planet(tyngde, planet)
    
elif funksjon == 20:
    print("Akselrasjon = kraft/masse\n")

    kraft_input()
    masse_input()
    svar = akselrasjon_kraft_masse(kraft, masse)

elif funksjon == 21:
    print("Masse = kraft/akselrasjon\n")

    kraft_input()
    akselrasjon_input()
    svar = masse_kraft_akselrasjon(kraft, akselrasjon)

elif funksjon == 22:
    print("Strekning = arbeid/kraft\n")

    arbeid_input()
    kraft_input()
    svar = strekning_arbeid_kraft(arbeid, kraft)

elif funksjon == 23:
    print("Kraft = arbeid/strekning\n")

    arbeid_input()
    strekning_input()
    svar = kraft_arbeid_effekt(arbeid, effekt)

elif funksjon == 24:
    print("Arbeid = effekt*tid\n")

    effekt_input()
    tid_input()
    svar = arbeid_effekt_tid(effekt, tid)

elif funksjon == 25:
    print("Tid = arbeid/effekt\n")

    arbeid_input()
    effekt_input()
    svar = tid_arbeid_effekt(arbeid_effekt)

elif funksjon == 3.14:
    print(f"Tror du at 3,14 er π? Feil, π = {np.pi}.")

else:
    while True:
        print('''ERROR
        404
        error
        There is an error
        ''')
    
#Svaret
print(f"\n\n\nSvaret på utregningen din er {svar}.")
