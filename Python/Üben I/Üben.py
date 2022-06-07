Alpha = 100
Beta = 300
Y = 222
X = 222
Gamma = Alpha + Beta - Y * X
print(Gamma)
print("Ich""\t tabe und" "\n mache einen Absatz")

Adler = 5
Geier = 4 
Meise = 4

if (Adler < Meise):
    print("Ein Adler ist kleiner als eine Meise")
elif (Geier == Meise):
    print("Ein Geier ist so groß wie eine Meise")
elif (Adler > Geier):
    print("Ein Adler ist größer als ein Geier")
else:
    print ("Alles weitere")

a = -50
while (a <= 50):
    print(a)
    a += 5
    if (a >= 45):
        print("break")
        break
a = 5
while (a <= 50):
    print(a)
    a += 5
    if (a == 10):
        print("Zeeehn")
        continue
    if (a == 20):
        print("Zwanzig")
        continue
    if (a == 45):
        print("Fünfundvierzig")
        break

Leben = 100
Schaden = 150

if (Leben < Schaden):
    print("Du bist tot")


def minusRechner(Zahl1, Zahl2):
    Ergebnis = Zahl1 - Zahl2
    print(Ergebnis)


minusRechner(99, 55)


def Satzbauen(Wort):
    print("du bist " + Wort)


Satzbauen("Lieb")

b = 12
while (b <= 100):
    print(b)
    b += 5

b = 10
while (b <= 100):
    print(b)
    b += 10
    if (b >= 100):
        break


def Rechner(Veni=int,Vedi=int,Vici=int):
    Caesar=Veni+Vedi+Vici
    print(Caesar)

Rechner(5,3,9)
Rechner(123,425,5436245)

Name="Bernd"
Stadt="Oer Erkenschweg"
Alter="50"
Lieblingsfarbe= "Blau"
Sportverein= "Schalke 04"


print("mein Name lautet " + Name )
print (Name, "kommt aus "+Stadt, "Er ist " +Alter, "Jahre alt")
print(Stadt, "ist nicht sehr schön "+Name, "fühlt sich sehr unwohl dort " +Name, "Herz schlägt seit "+Alter, "Jahren für " +Sportverein )


BlaueAugen=False

if BlaueAugen:
    print("Peter hat blaue Augen")
else:
    print("Peter hat grüne Augen")



for y in ("2", "3"):
    print((y))


for y in range(1, 11):
    print (y)







