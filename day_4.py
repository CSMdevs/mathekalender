import random
uitslag1 = False
uitslag2 = False
uitslag3 = False

while(uitslag1 == False or uitslag2 == False or uitslag3 == False):
    uitslag1 = False
    uitslag2 = False
    uitslag3 = False
    print(" ")
    
    
    icetown_goals = 5
    icetown_against = 1
    icetown_wins = 2
    icetown_losses = 1
    
    frostville_goals = 3
    frostville_against = 5
    frostville_wins = 2
    frostville_losses= 1

    glacierhampton_goals = 5
    glacierhampton_against = 6
    glacierhampton_wins = 1
    glacierhampton_losses = 2

    coldbury_goals = 4
    coldbury_against = 5
    coldbury_wins = 1
    coldbury_losses = 2

    total_matches = 6
    
    wedstrijden: ["Icetown win", "Icetown win", "Icetown loss", "Frostville win", "Frostville win", "Frostville loss", "Glacierhampton win", "Glacierhampton loss", "Glacierhampton loss", "Coldbuty win", "Coldbury loss", "Coldbury loss"]
    uitslagenlinks = []
    uitslagenrechts = []
    #icetown vs (1 = frostville, 2 = glacierhampton, 3 = coldbury)
    icevsfrost = False
    icevsglacier = False
    icevscold = False
    while(icevsfrost == False or icevsglacier == False or icevscold == False):
        gescoord = random.randint(0,icetown_goals)
        tegen = random.randint(0, icetown_against)
        
        #icetown win 1
        if(gescoord > tegen and uitslag1 == False and gescoord != 5):
            tegenstander = random.randint(1,3)

            #icetown vs frostville
            if(tegenstander == 1 and icevsfrost == False and frostville_against - gescoord > 0 and frostville_goals - tegen > 0):
                print("ICE VS FROST: " + str(gescoord) + ":" + str(tegen))
                uitslagenlinks.append(gescoord)
                uitslagenrechts.append(tegen)
                icetown_goals = icetown_goals - gescoord
                icetown_against = icetown_against - tegen
                frostville_goals = frostville_goals - tegen
                frostville_against = frostville_against - gescoord
                uitslag1 = True
                icevsfrost = True
                gescoord = random.randint(0,icetown_goals)
                tegen = random.randint(0, icetown_against)  
            
            #icetown vs glacierhampton
            elif(tegenstander == 2 and icevsglacier == False and glacierhampton_against - gescoord > 0 and glacierhampton_goals - tegen > 0):
                print("ICE VS GLACIER: " + str(gescoord) + ":" + str(tegen))
                uitslagenlinks.append(gescoord)
                uitslagenrechts.append(tegen)
                icetown_goals = icetown_goals - gescoord
                icetown_against = icetown_against - tegen
                glacierhampton_goals = glacierhampton_goals - tegen
                glacierhampton_against = glacierhampton_goals - gescoord
                uitslag1 = True
                icevsglacier = True
                gescoord = random.randint(0,icetown_goals)
                tegen = random.randint(0, icetown_against)

            elif(tegenstander == 2 and icevscold == False and coldbury_against - gescoord > 0 and coldbury_goals - tegen > 0):
                print("ICE VS COLD: " + str(gescoord) + ":" + str(tegen))
                uitslagenlinks.append(gescoord)
                uitslagenrechts.append(tegen)
                icetown_goals = icetown_goals - gescoord
                icetown_against = icetown_against - tegen
                coldbury_goals = coldbury_goals - tegen
                coldbury_against = coldbury_goals - gescoord
                uitslag1 = True
                icevscold = True
                gescoord = random.randint(0,icetown_goals)
                tegen = random.randint(0, icetown_against)
            else:
                gescoord = random.randint(0,icetown_goals)
                tegen = random.randint(0, icetown_against)
        
        #icetown win 2
        if(gescoord > tegen and uitslag2 == False and uitslag1 == True):
            tegenstander = random.randint(1,3)
                
            #icetown vs frostville
            if(tegenstander == 1 and icevsfrost == False and frostville_against - gescoord > 0 and frostville_goals - tegen > 0):
                print("ICE VS FROST: " + str(icetown_goals) + ":" + str(tegen))
                uitslagenlinks.append(icetown_goals)
                uitslagenrechts.append(tegen)
                icetown_goals = 0
                icetown_against = icetown_against - tegen
                frostville_goals = frostville_goals - tegen
                frostville_against = frostville_against - gescoord
                uitslag2 = True
                icevsfrost = True
                gescoord = random.randint(0,icetown_goals)
                tegen = random.randint(0, icetown_against)  
            
            #icetown vs glacierhampton
            elif(tegenstander == 2 and icevsglacier == False and glacierhampton_against - gescoord > 0 and glacierhampton_goals - tegen > 0):
                print("ICE VS GLACIER: " + str(icetown_goals) + ":" + str(tegen))
                uitslagenlinks.append(icetown_goals)
                uitslagenrechts.append(tegen)
                icetown_goals = 0
                icetown_against = icetown_against - tegen
                glacierhampton_goals = glacierhampton_goals - tegen
                glacierhampton_against = glacierhampton_goals - gescoord
                uitslag2 = True
                icevsglacier = True
                gescoord = random.randint(0,icetown_goals)
                tegen = random.randint(0, icetown_against)

            elif(tegenstander == 2 and icevscold == False and coldbury_against - gescoord > 0 and coldbury_goals - tegen > 0):
                print("ICE VS COLD: " + str(icetown_goals) + ":" + str(tegen))
                uitslagenlinks.append(icetown_goals)
                uitslagenrechts.append(tegen)
                icetown_goals = 0
                icetown_against = icetown_against - tegen
                coldbury_goals = coldbury_goals - tegen
                coldbury_against = coldbury_goals - gescoord
                uitslag2 = True
                icevscold = True
                gescoord = random.randint(0,icetown_goals)
                tegen = random.randint(0, icetown_against)
            else:
                gescoord = random.randint(0,icetown_goals)
                tegen = random.randint(0, icetown_against)
                
        
        #icetown loss 1
        if(gescoord < tegen and uitslag3 == False and uitslag1 == True and uitslag2 == True):
            uitslagen.append(str(gescoord) + str(tegen))
            icetown_goals = icetown_goals - gescoord
            icetown_against = icetown_against - tegen
            uitslag3 = True


#print(uitslagen)

#okeee zo moet het dus nu
#voor elke club is er natuurlijk gezegd hoeveel wins en losses
#elke keer als een random club wint, dan haalt ie een loss van een random partij af waartegen nog niet gespeeld is (misschien met een array ofzo)
#en dan haal je goals tegen en voor bij de tegenstander weg, en dan hoef je maar 6 simulaties te runnen
#als dat allemaal gedaan is dan checkt ie of verschillende dingen twee keer voorkomen
#en dan iets doen om het antwoord te krijgen