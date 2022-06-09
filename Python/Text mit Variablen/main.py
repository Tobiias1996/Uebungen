Name=input("Wie lautet dein Name?\n")

Alter=input("Wie alt bist du?\n")

Herkunft=input("Aus welchem Land kommst du?\n")

Stadt=input("In welcher Stadt wohnst du?\n")

Beruf=input("Was bist du beruflich?\n")

BerufStadt=input("In welcher Stadt arbeitest du?\n")

Groesse=input("Wie groß [in cm] bist du?\n")

Augenfarbe=input("Welche Farbe haben deine Augen?\n")

Haarfarbe=input("Welche Farbe haben deine Haare?\n")

Lieblingsessen=input("Was ist dein Lieblingsessen?\n")

Musik=input("Was ist deine Lieblingsmusik?\n")

Reiseziel=input("Wohin möchtest du unbedingt einmal reisen?\n")

#True oder False vor Run eingeben

StadtSchoen=False 

IchmagFußball=True

print("Hallo, mein Name lautet", Name, "und ich bin", Alter, "Jahre alt. Ich komme aus", Herkunft,".")
if StadtSchoen:
    print("Dort wohne ich im schönen", Stadt,".")
else:
    print("Dort wohne ich im nicht sehr schönen", Stadt, ".")
print("Von Beruf her bin ich", Beruf, "und arbeite in", BerufStadt, ". Ich bin", Groesse, "cm groß. Während meine Augen", Augenfarbe, "sind, ist meine Haar", Haarfarbe,"." )
print("Ich esse am liebsten", Lieblingsessen, "und höre sehr gerne", Musik,". Mein Traum ist es schon lange nach", Reiseziel, "zu reisen.")
if IchmagFußball:
    Verein=input("Welcher ist DEIN Verein?\n")
    print("Ich bin ein großer Fußball Fan. Mein Lieblingsverein ist eindeutig", Verein, ".")
else:
    Sport=input("Welchen Sport magst du am liebsten?\n")
    print=("Mit Fußball kann ich nicht viel anfangen. Ich bevorzuge", Sport, "." )