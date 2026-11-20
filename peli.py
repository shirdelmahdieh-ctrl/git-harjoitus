import random

vaihtoehdot = ["kivi", "paperi", "sakset"]

print("Tervetuloa Kivi, paperi, sakset -peliin!")

pelaaja = input("Valitse kivi, paperi tai sakset: ").lower()
tietokone = random.choice(vaihtoehdot)

print("Sinä valitsit:", pelaaja)
print("Tietokone valitsi:", tietokone)

if pelaaja not in vaihtoehdot:
    print("Virheellinen valinta!")
elif pelaaja == tietokone:
    print("Tasapeli!")
elif (pelaaja == "kivi" and tietokone == "sakset") or \
     (pelaaja == "paperi" and tietokone == "kivi") or \
     (pelaaja == "sakset" and tietokone == "paperi"):
    print("Voitit!")
else:
    print("Tietokone voitti!")

pelaajan_pisteet = 0
tietokoneen_pisteet = 0

if pelaaja in vaihtoehdot:
    if pelaaja == tietokone:
        print("Kumpikaan ei saa pisteitä.")
    elif (pelaaja == "kivi" and tietokone == "sakset") or \
         (pelaaja == "paperi" and tietokone == "kivi") or \
         (pelaaja == "sakset" and tietokone == "paperi"):
        pelaajan_pisteet += 1
    else:
        tietokoneen_pisteet += 1

print("Pelaajan pisteet:", pelaajan_pisteet)
print("Tietokoneen pisteet:", tietokoneen_pisteet)
