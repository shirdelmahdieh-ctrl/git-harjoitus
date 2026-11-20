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
