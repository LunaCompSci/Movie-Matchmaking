#Christina Nguyen, 2/6/21, calculates how likely you will like a movie you like based on your favorite movie

DIRECTOR = .20
LEAD_ACTOR = .20
DECADE = .1
CATEGORIES = .5

def main(): 
    titleFav = "When Marnie Was There" #First movie data
    directorFav = "Hiromasa Yonebayashi"
    lead_actorFav = "Sara Takatsuki"
    yearFav = 2014
    animeFav = True
    familyFav = True
    comedyFav = False
    dramaFav = True
    horrorFav = False
    romanceFav = False
    sciFiFav = False
    thrillerFav = False
    traitsFavTuple = (titleFav, directorFav, lead_actorFav, yearFav,\
                 animeFav, familyFav, comedyFav, dramaFav, horrorFav, romanceFav, sciFiFav, thrillerFav)
    

    titleComparison = "Hope" #second movie data
    directorComparison = "Lee Joon-ik"
    lead_actorComparison = "Lee Re"
    yearComparison = 2013
    animeComparison = False
    familyComparison = False
    comedyComparison = False
    dramaComparison = True
    horrorComparison = False
    romanceComparison = False
    sciFiComparison = False
    trillerComparison = False
    traitsComparisonTuple = (titleComparison, directorComparison, lead_actorComparison, yearComparison,\
                                animeComparison,familyComparison,comedyComparison,dramaComparison,horrorComparison,\
                                 romanceComparison,sciFiComparison,trillerComparison)
    
    overallProbability = calcLikeProbability(traitsFavTuple, traitsComparisonTuple)
    
    print("The probability the viewer will like the other movie is ", overallProbability * 100,"%", sep = '')   

def calcLikeProbability(traitsFavTuple, traitsComparisonTuple):
        titleFav,directorFav, lead_actorFav,yearFav,\
        animeFav,familyFav,comedyFav,dramaFav,horrorFav,romanceFav,sciFiFav,thrillerFav = traitsFavTuple #first movie tuple
        
        titleComparison, directorComparison, lead_actorComparison, yearComparison,\
        animeComparison,familyComparison,comedyComparison,dramaComparison,horrorComparison,\
        romanceComparison,sciFiComparison,thrillerComparison = traitsComparisonTuple #second movie tuple

        totalFavCategories = animeFav + familyFav + comedyFav + dramaFav + horrorFav + romanceFav + sciFiFav + thrillerFav #every true catgory is 1 and every false catgory is 0. this adds up the total amount of favorite categories
        favComparison = animeComparison + familyComparison + comedyComparison + dramaComparison + \
                        horrorComparison + romanceComparison + sciFiComparison + thrillerComparison
                
        matches = 0 #finds the matches
        if animeFav and animeComparison:
            matches = matches + 1
        if familyFav and familyComparison:
            matches = matches + 1
        if comedyFav and comedyComparison:
            matches = matches + 1
        if dramaFav and dramaComparison:
            matches = matches + 1
        if horrorFav and horrorComparison:
            matches = matches + 1
        if romanceFav and romanceComparison:
            matches = matches + 1
        if sciFiFav and sciFiComparison:
            matches = matches + 1
        if thrillerFav and thrillerComparison:
            matches = matches + 1

        if totalFavCategories == 0: #If totalFavCategories = 0 then there is a bug. This compensates it.
            categoryProbability = 0
        else: #accounts for categories
            categoryPercent = matches/totalFavCategories 
            categoryProbability = categoryPercent * CATEGORIES
   
        decadeProbability = calcDecadeProbability(yearFav, yearComparison) * DECADE

        if categoryProbability == 0: #If categoryProbability = 0 then there is a bug. This compensates it.
            overallProbability = decadeProbability

        overallProbability = decadeProbability + categoryProbability 

        if directorFav == directorComparison: #accounts for director
            overallProbability += DIRECTOR
            
        if lead_actorFav == lead_actorComparison: #accounts for lead actor
            overallProbability += LEAD_ACTOR

        return overallProbability 

def calcDecadeProbability(yearFav, yearComparison): #calculates decade probability

    yearFavDownRound = yearFav - 10
    yearFavUpRound = yearFav + 10
    first3DigitsOfYearFav = str(yearFav)[0:3]
    first3DigitsOfYearComparison = str(yearComparison)[0:3]
    if first3DigitsOfYearFav == first3DigitsOfYearComparison:
        return 1.0
    elif yearComparison in range(yearFavDownRound, yearFavUpRound):
        return 0.5
    else:
        yearComparison > yearFavUpRound or yearComparison < yearFavDownRound
        return 0.0

main()

#If I could do something different, I wish I could loop my long list of IF statements
#Another test case I did was I made all the categories False. This causes a bug on line 78 because 0/0 is undefined.
#to conpensate this lines 75-76 and 83-84 were programmed.
#A place where I got stuck was realizing that I had to set matches to 0 which I asked a tutor about.
#Another test case I did was make yearFav and yearComparison in the same. I realized I had two errors.
#1.) On line 85 I was multiplying decadeProbability and categoryProbability.
#2.) On line 80 I was missing * DECADE
#Both errors were due to not fully understanding the required math behind the program
#Another test case I did was make all the catgories False, make the years of the two movies non-adjacent, the directors different and the lead actors the same.
#I did this to see if there was anything wrong with the lead actor calculation. I exspected to get 20% and got 20%.
#I did another test with the same conditions except the lead actors were different and the directors were the same.
#I also did this to see if there was anything wrong with the director calculation. I exspected to get 20% and got 20%.
#For my last test I passed the same movie to see if I would get 100% and I did.

