WelcheSchwierigkeit=input("Wähle ein Schwierigkeit aus. 1: Anfänger. 2: Könner\n")

if (WelcheSchwierigkeit=="1"):
    print ("Du hast die Schwierigkeit 'Anfänger' gewählt")
    AnfängerFrageEins=input("Was ist die Hauptstadt von Deutschland?\n 1: Hamburg\n 2: München\n 3: Berlin\n") 
    if (AnfängerFrageEins=="3"):
        print ("Korrekt! Berlin ist die Hauptsadt von Deutschland! Interessanterweise zieht Berlin, im Gegensatz zu vielen anderen Hauptstädten das BIP des Landes ein wenig runter.Kommen wir zur nächsten Frage")
        AnfängerFrageZwei=input("Was ist die Hauptstadt von Frankreich?\n 1: Lyon\n 2: Paris\n 3: Brüssel\n")
        if (AnfängerFrageZwei=="2"):
            print ("So ist es. Paris ist die Hauptstadt von Frankreich und eine der meistbesuchtesten Städte weltweit. Nächste Frage:")
            AnfängerFrageDrei=input("Was ist die Hauptstadt von Spanien?\n 1: Barcelona\n 2: Madrid\n 3: Lissabon\n")
            if (AnfängerFrageDrei=="2"):
                print ("Wieder richtig! Madrid ist seit 1561 die Hauptstadt Spaniens. Vierte Frage:")
                AnfängerFrageVier=input ("Welches Land ist das flächenmäßig größte auf der Welt?\n 1: Russland\n 2: Kanada\n 3: Australien\n")
                if (AnfängerFrageVier=="1"):
                    print("Auch das stimmt. Russland ist mit einer Fläche von rund 17 Millionen km² deutlich größer als das zweitplatzierte Kanda (knapp 10 Millionen km²)")
                    AnfängerFrageFünf=input("Wir kennen nun das flächengrößte Land der Welt. Doch was ist das bevölkerungsreichste?\n 1: Indien\n 2: USA\n 3: China\n")
                    if (AnfängerFrageFünf=="3"):
                        print("Genau! In China leben mit 1,412 Milliarden Menschen die meisten. Indien folgt mit 1,38 Milliarden knapp dahinter. Kommen wir zur sechsten Frage:")
                        AnfängerFrageSechs=input("Wie viele Kontinente gibt es?\n 1: Fünf\n 2: Sechs\n 3: Sieben\n")
                        if (AnfängerFrageSechs=="3"):
                            print("Ganz genau! Die Kontinente lauten: Nordamerika, Südamerika, Europa, Afrika, Asien, Australien/Ozeaninen und Antarktika. Du bist bereits weit gekommen. Fahren wir fort:")
                            AnfängerFrageSieben=input("Welches dieser Länder gehört nicht zu Europa?\n 1: Albanien\n 2: Aserbaidschan\n 3: Kasachstan\n")
                            if (AnfängerFrageSieben=="3"):
                                print ("Richtig! Kasachstan gehört zum Kontinent Asien. Du hast es bald geschafft!")
                                AnfängerFrageAcht=input("Welcher Fluss ist der längste der Welt?\n 1: Der Amazonas\n 2: Der Nil\n 3. Der Mississippi\n")
                                if (AnfängerFrageAcht=="2"):
                                    print ("Der Nil ist mit einer Länge von 6.650 km der längste Fluss unserer Erde. Er fließt von Ruanda bis ins Mittelmeer. Kommen wir zur vorletzten Frage:")
                                    AnfängerFrageNeun=input("Welcher deutsche Nicht-Stadtstaat ist das bevölkerungskleinste Bundesland?\n 1: Mecklenburg-Vorpommern\n 2: Das Saarland\n 3: Brandenburg\n")
                                    if (AnfängerFrageNeun=="2"):
                                        print("Ja, das Saarland ist mit einer Einwohnerzahl von knapp einer Millionen sogar kleiner als die Stadtstaaten Berlin und Hamburg. Wir kommen zur letzten Frage:")
                                        AnfängerFrageZehn=input("An welchen Kontinent grenz Europa NICHT?\n 1: Südamerika\n 2: Afrika\n 3: Antarktika\n")
                                        if (AnfängerFrageZehn)=="3":
                                            print ("Gute Arbeit! Europa teilt sich sowohl mit Afrika (durch die spanische Enklave Ceuta), als auch mit Südamerika (Französisch Guyana) eine Grenze, jedoch nicht mit Antarktika. Das war's. Versuche dich doch nun an dem Könner Quiz.")
                                        else:
                                            print ("Kurz vor dem Ende scheiterst du. Sehr schade! Aber vielleicht gelingt es dir ja beim nächsten Mal!")
                                    else:
                                        print ("Schade, du hattest es fast geschafft! Versuche es doch noch einmal")
                                else:
                                    print ("Das stimmt nicht, vielleicht schaffst du es ja beim nächsten Mal!")    
                            else:
                                print ("Nein, versuche es doch noch einma.l")
                        else:
                            print("Leider falsch. Versuche es doch noch einmal.")
                    else:
                        print("Nein, versuche es doch noch einmal.")    
            else:
                print ("Das stimmt nicht. Versuche es doch noch einmal")
    else:
        print ("Falsch! Versuche es doch noch einmal.")  

elif(WelcheSchwierigkeit=="2"):
    print("Du bezeichnest dich also als Könner! Wir wollen doch einmal sehen, ob du wirklich einer bist. Erste Frage:")
    KoennerFrageEins=input("Was ist die Hauptstadt von Serbien?\n 1: Belgrad\n 2: Sarajevo\n 3: Ljubljana\n")
    if (KoennerFrageEins=="1"):
        print("Ganz genau! Sarajevo ist die Hauptstadt von Bosnien-Herzegowina und Ljubljana von Slowenien. Weiter geht's:")
        KoennerFrageZwei=input("Zu welchem Land gehört Grönland?\n 1: Grönland ist unabhängig\n 2: Dänemark\n 3: Island\n")
        if (KoennerFrageZwei=="2"):
            print("Zwar ist Grönland bestrebt unabhängig zu werden. Doch momentan ist es noch immer mit Dänemark assoziiert! Schauen wir uns die dritte Frage an:")
            KoennerFrageDrei=input("Welches dieser Länder gehört zum Baltikum?\n 1: Finnland\n 2: Polen\n 3: Litauen\n")
            if (KoennerFrageDrei=="3"):
                print ("Polen und Finnland gehören nicht zum Baltikum. Neben Litauen bilden Estland und Lettland das Baltikum. Korrekte Antwort!")
                KoennerFrageVier=input("Welche Farbe kommt auf den meisten Landesflaggen vor?\n 1: Rot\n 2: Blau\n 3: Grün\n")
                if (KoennerFrageVier=="1"):
                    print("Richtig. Sieh dir nur einmal eine Übersicht an und dir wird sicherlich sofort auffallen, dass die Farbe Rot auf den meisten Flaggen zu erkennen ist.")
                    KoennerFrageFuenf=input("Welches dieser Länder zählt NICHT zur Region Südostasien?\n 1: Myanmar\n 2: Bangladesch\n 3: Brunei\n")
                    if (KoennerFrageFuenf=="2"):
                        print("Sehr gut. Bangladesch zählt man offiziell zur Region Südasien. Bisher läuft es doch ganz gut. gehen wir weiter zur sechsten Frage:")
                        KoennerFrageSechs=input("Was ist die Hauptstadt des zweitbevölkerungsreichsten Land in Skandinavien?\n 1: Oslo\n 2. Helsinki\n 3. Kopenhagen\n")
                        if (KoennerFrageSechs=="3"):
                            print("Richtig! Dänemark hat knapp mehr Einwohner als Finnland und Norwegen. Das meistbevölkerste Land Skandinaviens ist übrigens Schweden! In Island leben mit Abstand die wenigsten Skandinavier. Frage Sieben:")
                            KoennerFrageSieben=input("An welches der folgenden Länder grenzt Russland NICHT.\n 1: Nordkorea\n 2: Polen\n 3: Usbekistan\n")
                            if (KoennerFrageSieben=="3"):
                                print("Langsam wird es kompliziert oder? Tatsächlich teilt sich Russland eine weniger als 50 km lange Grenze mit Nordkorea und dank seiner Exklave Kaliningrad auch eine mit Polen")
                                KoennerFrageAcht= input("Auf welcher der drei folgenden Landesflaggen gibt es KEINEN Stern.\n 1: Angola \n 2: Pakistan\n 3: Argentinien\n")
                                if (KoennerFrageAcht=="3"):
                                    print("Genau. Auf der argentinischen Flagge ist eine Sonne zu sehen. Wir nähern uns dem Finale:")
                                    KoennerFrageNeun=input("Wie viele Länder werden komplett von der Republik Südafrika umschlossen?\n 1: 1\n 2: 2\n 3: 3\n")
                                    if (KoennerFrageNeun=="2"):
                                        print ("Die Republik Südafrika umschließt die Länder Lesotho und Swasiland komplett. Deine Antwort war also korrekt. Bist du bereit für die letzte Frage?")
                                        KoennerFrageZehn=input("Welche der folgenden Metropolregionen gehört NICHT zu den fünftgrößten der Welt?\n 1: Shanghai\n 2: Delhi\n 3: Sao Paulo\n")
                                        if (KoennerFrageZehn=="1"):
                                            print("Herzlichen Glückwunsch! Du bist ein wahrhaftiger Geographie Könner. Shanghai ist 'nur' die achtgrößte Metropolregion auf der Erde.")
                                        else:
                                            print ("Es ist keine Schande im Finale falschzuliegen. Wenn dich diese Niederlage ärgert, kannst du es gerne noch einmal probieren!")
                                    else:
                                        print("Bedauerlicherweise war deine Antwort falsch und das bei der neunten Frage. Willst du es bis ins Finale schaffen? Dann versuche es erneut")
                                else:
                                    print("So kurz vor dem Finale ist dir ein Fehler unterlaufen. Du kannst es aber natürlich noch einmal probieren")
                            else:
                                print("Die Frage war zugegeben schwer. Hier kann sich auch einmal ein Könner irren. Versuche es erneut!")    
                        else:
                            print("Nein. Versuche es erneut oder gibst du dich etwa geschlagen?")
                    else:
                        print("Die Frage war zugegeben schwer. Hier kann sich auch einmal ein Könner irren. Versuche es erneut!")
                else:
                    print("Falsch! Versuche es doch noch einmal.")
            else:
                print ("Leider falsch. Versuche es doch noch einmal oder beginne mit den Anfänger Fragen.")    
        else:
            print("Nein, versuche es doch noch einmal.")    
    else:
        print ("Ein Fehler, gleich bei der ersten Frage? Vielleicht solltest du doch mit den Anfänger Fragen beginnen?")
else:
    print("fehlerhafte Eingabe")

      


    