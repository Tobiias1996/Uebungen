WelcheSchwierigkeit=input("Wähle ein Schwierigkeit aus. 1: Anfänger. 2:Schwer: Könner\n")

 
    




if (WelcheSchwierigkeit=="1"):
    print ("Du hast die Schwierigkeit 'Anfänger' gewählt")
    AnfängerFrageEins=input("Was ist die Hauptstadt von Deutschland?\n 1: Hamburg\n 2: München\n 3: Berlin\n") 
    if (AnfängerFrageEins=="3"):
        print ("Korrekt! Berlin ist die Hauptsadt von Deutschland! Interessanterweise zieht Berlin, im Gegensatz zu vielen anderen Hauptstädten des BIP Landes ein wenig runter.Kommen wir zur nächsten Frage")
        AnfängerFrageZwei=input("Was ist die Hauptstadt von Frankreich?\n 1: Lyon\n 2: Paris\n 3: Brüssel\n")
        if (AnfängerFrageZwei=="2"):
            print ("So ist es. Paris ist die Hauptstadt von Frankreich und eine der meistbesuchtesten Städte weltweit. Nächste Frage:")
            AnfängerFrageDrei=input("Was ist die Hauptstadt von Spanien?\n 1: Barcelona\n 2: Madrid\n 3: Lissabon\n")
            if (AnfängerFrageDrei=="2"):
                print ("Wieder richtig! Madrid ist seit 1561 die Hauptstadt Spaniens. Dritte Frage:")
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
                                
                        else:
                            print("Leider falsch. Es gibt insgesamt sieben Kontinente: Nordamerika, Südamerika, Europa, Afrika, Asien, Australien/Ozeaninen und Antarktika")
                    else:
                        print("Nein, die meisten Menschen leben in China.")    
            else:
                print ("Das stimmt nicht. Die Hauptstadt von Spanien ist Madrid")
    else:
        print ("Falsch! Die Hauptstadt von Deutschland ist Berlin.")  

elif(WelcheSchwierigkeit=="2"):
    print("Platzhalter")
else:
    print("fehlerhafte Eingabe")
      


    