import random
uitslag1 = False
uitslag2 = False
uitslag3 = False
uitslag4 = False
uitslag5 = False
uitslag6 = False

while(uitslag1 == False or uitslag2 == False or uitslag3 == False or uitslag4 == False or uitslag5 == False):
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

    wedstrijden: ["Icetown win", "Icetown win", "Icetown loss", "Frostville win", "Frostville win", "Frostville loss", "Glacierhampton win", "Glacierhampton loss", "Glacierhampton loss", "Coldbuty win", "Coldbury loss", "Coldbury loss"]
    uitslagenlinks = []
    uitslagenrechts = []

    icevsfrost = False
    icevsglacier = False
    icevscold = False
    frostvsglacier = False
    frostvscold = False
    coldvsglacier = False

    uitslag1 = False
    uitslag2 = False
    uitslag3 = False
    uitslag4 = False
    uitslag5 = False
    uitslag6 = False

    match1 = ""
    match2 = ""
    match3 = ""
    match4 = ""
    match5 = ""
    match6 = ""

    goed = False
    while(icevsfrost == False or icevsglacier == False or icevscold == False or frostvsglacier == False or frostvscold == False):
        gescoord = random.randint(0, icetown_goals)
        tegen = random.randint(0, icetown_against)
        
        #icetown win 1
        if(gescoord > tegen and uitslag1 == False and gescoord != icetown_goals and tegen != icetown_against):
            tegenstander = random.randint(1,3)

            #icetown vs frostville
            if(tegenstander == 1 and icevsfrost == False and frostville_against - gescoord >= 0 and frostville_goals - tegen >= 0):
                print("ICE VS FROST 1: " + str(gescoord) + ":" + str(tegen))
                match1 = "IvsF"
                uitslagenlinks.append(gescoord)
                uitslagenrechts.append(tegen)
                icetown_goals = icetown_goals - gescoord
                icetown_against = icetown_against - tegen
                icetown_wins = icetown_wins - 1
                frostville_goals = frostville_goals - tegen
                frostville_against = frostville_against - gescoord
                frostville_losses = frostville_losses - 1
                uitslag1 = True
                icevsfrost = True
                gescoord = random.randint(0,icetown_goals)
                tegen = random.randint(0, icetown_against)  
            
            #icetown vs glacierhampton
            elif(tegenstander == 2 and icevsglacier == False and glacierhampton_against - gescoord >= 0 and glacierhampton_goals - tegen >= 0):
                print("ICE VS GLACIER 1: " + str(gescoord) + ":" + str(tegen))
                match1 = "IvsG"
                uitslagenlinks.append(gescoord)
                uitslagenrechts.append(tegen)
                icetown_goals = icetown_goals - gescoord
                icetown_against = icetown_against - tegen
                icetown_wins = icetown_wins - 1
                glacierhampton_goals = glacierhampton_goals - tegen
                glacierhampton_against = glacierhampton_goals - gescoord
                glacierhampton_losses = glacierhampton_losses - 1
                uitslag1 = True
                icevsglacier = True
                gescoord = random.randint(0,icetown_goals)
                tegen = random.randint(0, icetown_against)

            #icetown vs coldbury
            elif(tegenstander == 2 and icevscold == False and coldbury_against - gescoord >= 0 and coldbury_goals - tegen >= 0):
                print("ICE VS COLD 1: " + str(gescoord) + ":" + str(tegen))
                match1 = "IvsC"
                uitslagenlinks.append(gescoord)
                uitslagenrechts.append(tegen)
                icetown_goals = icetown_goals - gescoord
                icetown_against = icetown_against - tegen
                icetown_wins = icetown_wins - 1
                coldbury_goals = coldbury_goals - tegen
                coldbury_against = coldbury_goals - gescoord
                coldbury_losses = coldbury_losses - 1
                uitslag1 = True
                icevscold = True
                gescoord = random.randint(0,icetown_goals)
                tegen = random.randint(0, icetown_against)
            else:
                gescoord = random.randint(0,icetown_goals)
                tegen = random.randint(0, icetown_against)
        
        #icetown win 2
        if(gescoord > tegen and uitslag2 == False and uitslag1 == True and tegen != icetown_against):
            tegenstander = random.randint(1,3)
                
            #icetown vs frostville
            if(tegenstander == 1 and icevsfrost == False and frostville_against - gescoord >= 0 and frostville_goals - tegen >= 0):
                print("ICE VS FROST: " + str(icetown_goals) + ":" + str(tegen))
                match2 = "IvsF"
                uitslagenlinks.append(icetown_goals)
                uitslagenrechts.append(tegen)
                icetown_goals = 0
                icetown_against = icetown_against - tegen
                icetown_wins = icetown_wins - 1
                frostville_goals = frostville_goals - tegen
                frostville_against = frostville_against - gescoord
                frostville_losses = frostville_losses - 1
                uitslag2 = True
                icevsfrost = True
                gescoord = random.randint(0,icetown_goals)
                tegen = random.randint(0, icetown_against)  
            
            #icetown vs glacierhampton
            elif(tegenstander == 2 and icevsglacier == False and glacierhampton_against - gescoord >= 0 and glacierhampton_goals - tegen >= 0):
                print("ICE VS GLACIER: " + str(icetown_goals) + ":" + str(tegen))
                match2 = "IvsG"
                uitslagenlinks.append(icetown_goals)
                uitslagenrechts.append(tegen)
                icetown_goals = 0
                icetown_against = icetown_against - tegen
                icetown_wins = icetown_wins - 1
                glacierhampton_goals = glacierhampton_goals - tegen
                glacierhampton_against = glacierhampton_goals - gescoord
                glacierhampton_losses = glacierhampton_losses - 1
                uitslag2 = True
                icevsglacier = True
                gescoord = random.randint(0,icetown_goals)
                tegen = random.randint(0, icetown_against)
            
            #icetown vs coldbury
            elif(tegenstander == 2 and icevscold == False and coldbury_against - gescoord >= 0 and coldbury_goals - tegen >= 0):
                print("ICE VS COLD: " + str(icetown_goals) + ":" + str(tegen))
                match2 = "IvsC"
                uitslagenlinks.append(icetown_goals)
                uitslagenrechts.append(tegen)
                icetown_goals = 0
                icetown_against = icetown_against - tegen
                icetown_wins = icetown_wins - 1
                coldbury_goals = coldbury_goals - tegen
                coldbury_against = coldbury_goals - gescoord
                coldbury_losses = coldbury_losses - 1
                uitslag2 = True
                icevscold = True
                gescoord = random.randint(0,icetown_goals)
                tegen = random.randint(0, icetown_against)
            else:
                gescoord = random.randint(0,icetown_goals)
                tegen = random.randint(0, icetown_against)
                
        
        #icetown loss 1
        if(gescoord < tegen and uitslag3 == False and uitslag1 == True and uitslag2 == True):
            tegenstander = random.randint(1,3)

            #icetown vs frostville
            if(tegenstander == 1 and icevsfrost == False and frostville_against - gescoord >= 0 and frostville_goals - tegen >= 0):
                print("ICE VS FROST: " + str(gescoord) + ":" + str(tegen))
                match3 = "IvsF"
                uitslagenlinks.append(gescoord)
                uitslagenrechts.append(tegen)
                icetown_goals = icetown_goals - gescoord
                icetown_against = icetown_against - tegen
                icetown_losses = icetown_losses - 1
                frostville_goals = frostville_goals - tegen
                frostville_against = frostville_against - gescoord
                frostville_wins = frostville_wins - 1
                uitslag3 = True
                icevsfrost = True
                gescoord = random.randint(0,icetown_goals)
                tegen = random.randint(0, icetown_against)  
            
            #icetown vs glacierhampton
            elif(tegenstander == 2 and icevsglacier == False and glacierhampton_against - gescoord >=0 and glacierhampton_goals - tegen >= 0):
                print("ICE VS GLACIER: " + str(gescoord) + ":" + str(tegen))
                match3 = "IvsG"
                uitslagenlinks.append(gescoord)
                uitslagenrechts.append(tegen)
                icetown_goals = icetown_goals - gescoord
                icetown_against = icetown_against - tegen
                icetown_losses = icetown_losses - 1
                glacierhampton_goals = glacierhampton_goals - tegen
                glacierhampton_against = glacierhampton_goals - gescoord
                glacierhampton_wins = glacierhampton_wins - 1
                uitslag3 = True
                icevsglacier = True
                gescoord = random.randint(0,icetown_goals)
                tegen = random.randint(0, icetown_against)

            elif(tegenstander == 2 and icevscold == False and coldbury_against - gescoord >= 0 and coldbury_goals - tegen >= 0):
                print("ICE VS COLD: " + str(gescoord) + ":" + str(tegen))
                match2 = "IvsC"
                uitslagenlinks.append(gescoord)
                uitslagenrechts.append(tegen)
                icetown_goals = icetown_goals - gescoord
                icetown_against = icetown_against - tegen
                icetown_losses = icetown_losses - 1
                coldbury_goals = coldbury_goals - tegen
                coldbury_against = coldbury_goals - gescoord
                coldbury_wins = coldbury_wins - 1
                uitslag3 = True
                icevscold = True
                gescoord = random.randint(0,icetown_goals)
                tegen = random.randint(0, icetown_against)
            else:
                gescoord = random.randint(0,icetown_goals)
                tegen = random.randint(0, icetown_against)

    
    
    
    
    gescoord = random.randint(0, frostville_goals)
    tegen = random.randint(0, frostville_against)
    
    #frostville wins both
    if(frostville_wins == 2 and gescoord > tegen and frostville_goals - gescoord > frostville_against - tegen):
        tegenstander = random.randint(1,2) #1 = glacier and #2 is cold
        
        #frostville vs glacier
        if(tegenstander == 1 and gescoord != frostville_goals and tegen != frostville_against and glacierhampton_goals - tegen >= 0 and glacierhampton_against - gescoord >= 0 and coldbury_goals - tegen >= 0 and coldbury_against - gescoord >= 0):
            print("FROST VS GLACIER: " + str(gescoord) + ":" + str(tegen))
            match4 = "FvsG"
            uitslagenlinks.append(gescoord)
            uitslagenrechts.append(tegen)
            frostville_goals = frostville_goals - gescoord
            frostville_against = frostville_against - tegen
            frostville_wins = frostville_wins - 1
            glacierhampton_goals = glacierhampton_goals - tegen
            glacierhampton_against = glacierhampton_against - gescoord
            glacierhampton_losses = 0
            uitslag4 = True
            frostvsglacier = True
            
            gescoord = frostville_goals
            tegen = frostville_against
            
            print("FROST VS COLD: " + str(gescoord) + ":" + str(tegen))
            match4 = "FvsC"
            uitslagenlinks.append(gescoord)
            uitslagenrechts.append(tegen)
            frostville_goals = 0
            frostville_against = 0
            frostville_wins = 0
            coldbury_goals = coldbury_goals - tegen
            coldbury_against = coldbury_against - gescoord
            coldbury_losses = 0
            uitslag5 = True
            frostvscold = True
        
        #frostville vs coldbury
        elif(tegenstander == 2 and gescoord != frostville_goals and tegen != frostville_against and glacierhampton_goals - tegen >= 0 and glacierhampton_against - gescoord >= 0 and coldbury_goals - tegen >= 0 and coldbury_against - gescoord >= 0):
            print("FROST VS COLD: " + str(gescoord) + ":" + str(tegen))
            match4 = "FvsC"
            uitslagenlinks.append(gescoord)
            uitslagenrechts.append(tegen)
            frostville_goals = 0
            frostville_against = 0
            frostville_wins = 0
            coldbury_goals = coldbury_goals - tegen
            coldbury_against = coldbury_against - gescoord
            coldbury_losses = 0
            uitslag4 = True
            frostvscold = True
            gescoord = frostville_goals
            tegen = frostville_against
            
            print("FROST VS GLACIER: " + str(gescoord) + ":" + str(tegen))
            match5 = "FvsG"
            uitslagenlinks.append(gescoord)
            uitslagenrechts.append(tegen)
            frostville_goals = frostville_goals - gescoord
            frostville_against = frostville_against - tegen
            frostville_wins = frostville_wins - 1
            glacierhampton_goals = glacierhampton_goals - tegen
            glacierhampton_against = glacierhampton_against - gescoord
            glacierhampton_losses = 0
            uitslag5 = True
            frostvsglacier = True
            

        
    elif(frostville_wins == 1 and gescoord > tegen):
        if(tegen != frostville_against and glacierhampton_goals - tegen >= 0 and glacierhampton_against - gescoord >= 0 and coldbury_wins > 0 and coldbury_goals - tegen >= 0 and coldbury_against - gescoord >= 0):
            print("FROST VS GLACIER: " + str(gescoord) + ":" + str(tegen))
            match4 = "FvsG"
            uitslagenlinks.append(gescoord)
            uitslagenrechts.append(tegen)
            frostville_goals = frostville_goals - gescoord
            frostville_against = frostville_against - tegen
            frostville_wins = 0
            glacierhampton_goals = glacierhampton_goals - tegen
            glacierhampton_against = glacierhampton_against - gescoord
            glacierhampton_losses = 0
            uitslag4 = True
            frostvsglacier = True
            gescoord = frostville_goals
            tegen = frostville_against

            print("FROST VS COLD: " + str(gescoord) + ":" + str(tegen))
            match4 = "FvsC"
            uitslagenlinks.append(gescoord)
            uitslagenrechts.append(tegen)
            frostville_goals = 0
            frostville_against = 0
            frostville_losses = 0
            coldbury_goals = coldbury_goals - tegen
            coldbury_against = coldbury_against - gescoord
            coldbury_wins = 0
            uitslag5 = True
            frostvscold = True
        
        elif(tegen != frostville_against and coldbury_goals - tegen >= 0 and coldbury_against - gescoord >= 0 and glacierhampton_wins > 0 and coldbury_goals - tegen >= 0 and coldbury_against - gescoord >= 0):
            print("FROST VS COLD: " + str(gescoord) + ":" + str(tegen))
            match4 = "FvsC"
            uitslagenlinks.append(gescoord)
            uitslagenrechts.append(tegen)
            frostville_goals = frostville_goals - gescoord
            frostville_against = frostville_against - tegen
            frostville_wins = 0
            coldbury_goals = coldbury_goals - tegen
            coldbury_against = coldbury_against - gescoord
            coldbury_losses = 0
            uitslag4 = True
            frostvscold = True
            gescoord = frostville_goals
            tegen = frostville_against

            print("FROST VS GLACIER: " + str(gescoord) + ":" + str(tegen))
            match4 = "FvsG"
            uitslagenlinks.append(gescoord)
            uitslagenrechts.append(tegen)
            frostville_goals = 0
            frostville_against = 0
            frostville_losses = 0
            glacierhampton_goals = glacierhampton_goals - tegen
            glacierhampton_against = glacierhampton_against - gescoord
            glacierhampton_wins = 0
            uitslag5 = True
            frostvsglacier = True  
        else:
            gescoord = random.randint(0, frostville_goals)
            tegen = random.randint(0, frostville_against)
    else:
        gescoord = random.randint(0, frostville_goals)
        tegen = random.randint(0, frostville_against)
            