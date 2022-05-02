from types import MethodType
import time


class Director:
    def __init__(my, name, movie, year, deathyear, quote, award):
        my.name = name
        my.movie = movie
        my.year = year
        my.deathyear = deathyear
        my.quote = quote
        my.award = award

    def intro(self):
        print("Directors")
        print("Name:", self.name)
        print("Movie:", self.movie)
        print("Release year of the movie:", self.year)
        print("Award: ", self.award)
        print("Year of death: ", self.deathyear)

    def dquote(self):
        print(self.name, "'s quote: ", self.quote)

    def doYoulike(self):
        a = input("Do you like this director? (y or n)")
        if a == 'n':
            print("Pity You")
        elif a == 'y':
            print("Good for you")

        print("")
        print("")
        print("")
        print("")


director_1 = Director('Alfred Hitchcock', 'Psycho', 1964, 1980,
                      '“There is no terror in the bang, only the anticipation of it.”',
                      'Golden Globe – Best Supporting Actress')  # '“There is no terror in the bang, only the anticipation of it.”','Golden Globe – Best Supporting Actress'
director_2 = Director('Stanley Kubrick', 'A Clockwork Orange', 1971, 1999,
                      '“If it can be written, or thought, it can be filmed.”',
                      'Venice Film Festival –Pasinetti')  # ,'“If it can be written, or thought, it can be filmed.”','Venice Film Festival –Pasinetti'
director_3 = Director('Kátia Lund ', 'City of God ', 2002, ' Still Alive', ' Sorry, s/he doesnt have a quot',
                      'Academy Award – Best Director')  # ,'-','-','Academy Award – Best Director'
director_4 = Director('Christopher Nolan', 'Dark Knight', 2008, ' Still Alive', ' Sorry, s/he doesnt have a quot',
                      'Academy Award – Best Supporting Actor')  # ,'-' ,'-' ,'Academy Award – Best Supporting Actor'
director_5 = Director('Nuri Bilge Ceylan', 'Kıs Uykusu ', 2014, ' Still Alive', ' Sorry, s/he doesnt have a quot',
                      'Cannes Film Festival –Palme d’Or')  # , '-','-' ,'Cannes Film Festival –Palme d’Or'
director_6 = Director('Frank Derebont', 'Shawshank Redemption', 1994, ' Still Alive',
                      ', Sorry, s/he doesnt have a quot', ' None')  # ,'-','-','-'

# print(director_
director_1.intro()
director_1.dquote()
director_1.doYoulike()
time.sleep(1)

director_2.intro()
director_2.dquote()
director_2.doYoulike()
time.sleep(1)

director_3.intro()
director_3.dquote()
director_3.doYoulike()
time.sleep(1)

director_4.intro()
director_4.dquote()
director_4.doYoulike()
time.sleep(1)

director_5.intro()
director_5.dquote()
director_5.doYoulike()
time.sleep(1)

director_6.intro()
director_6.dquote()
director_6.doYoulike()
time.sleep(1)
