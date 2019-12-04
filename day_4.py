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

    frostville_goals = 3
    frostville_against = 5
    frostville_wins = 2

    glacierhampton_goals = 5
    glacierhampton_against = 6
    glacierhampton_wins = 1

    coldbury_goals = 4
    coldbury_against = 5
    coldbury_wins = 1
    
    wedstrijden: ["Icetown win", "Icetown lin", "Icetown loss", "Frostville win", "Frostville win", "Frostville loss", "Glacierhampton win", "Glacierhampton loss", "Glacierhampton loss", "Coldbuty win", "Coldbury loss", "Coldbury loss"]
    uitslagen = []

    gescoord = random.randint(0,icetown_goals)
    tegen = random.randint(0, icetown_against)
    
    #icetown vs X
    if(gescoord > tegen):
        if(uitslag1 == False):
            uitslagen.append(str(gescoord) + str(tegen))
            icetown_goals = icetown_goals - gescoord
            icetown_against = icetown_against - tegen
            uitslag1 = True
            gescoord = random.randint(0,icetown_goals)
            tegen = random.randint(0, icetown_against)
    
    if(gescoord > tegen):
        if(uitslag2 == False and uitslag1 == True):
            uitslagen.append(str(icetown_goals) + str(tegen))
            icetown_goals = 0
            icetown_against = icetown_against - tegen
            uitslag2 = True
            gescoord = random.randint(0,icetown_goals)
            tegen = random.randint(0, icetown_against)

    if(gescoord < tegen):
        if(uitslag3 == False and uitslag1 == True and uitslag2 == True):
            uitslagen.append(str(gescoord) + str(tegen))
            icetown_goals = icetown_goals - gescoord
            icetown_against = icetown_against - tegen
            uitslag3 = True
print(uitslagen)

#okeee zo moet het dus nu
#voor elke club is er natuurlijk gezegd hoeveel wins en losses
#elke keer als een random club wint, dan haalt ie een loss van een random partij af waartegen nog niet gespeeld is (misschien met een array ofzo)
#en dan haal je goals tegen en voor bij de tegenstander weg, en dan hoef je maar 6 simulaties te runnen
#als dat allemaal gedaan is dan checkt ie of verschillende dingen twee keer voorkomen
#en dan iets doen om het antwoord te krijgen