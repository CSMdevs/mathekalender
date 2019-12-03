ga_door = True
#(1.1).is_integer()
eind = 1
while(ga_door):
    print(" ")
    print("Eind: " + str(eind))
    
    ochtend = (eind * 5) + 1
    print("Ochtend: " + str(ochtend))
    
    ulli = ((ochtend / 4) * 5) + 1
    print("Ulli: " + str(ulli))
    
    if((ulli).is_integer()):
        mika = ((ulli / 4) * 5) + 1
        print("Mika: " + str(mika))
        
        if((mika).is_integer()):
            luca = ((mika / 4) * 5) + 1
            print("Luca: " + str(luca))
            
            if((luca).is_integer()):
                kim = ((luca / 4) * 5) + 1
                print("Kim: " + str(kim))

                if((kim).is_integer()):
                    charlie = ((kim / 4) * 5) + 1
                    print("Charlie: " + str(charlie))
                    if((charlie).is_integer()):
                        ga_door = False
                        antwoord = ((kim - 1) / 5) + eind
                        print("Antwoord: " + str(antwoord))
                    else:
                        eind = eind + 1
                    
                else:
                    eind = eind + 1
            else:
                eind = eind + 1

            #charlie
        else:
            eind = eind + 1

    else:
        eind = eind + 1
