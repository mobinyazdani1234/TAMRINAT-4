class Footbalist:

    def init(self, first_name, last_name, number, height, weight):
        
        self.first_name = first_name

        self.last_name = last_name

        self.number = number

        self.height = height

        self.weight = weight


    def player_first_number(self):
        return('The player first name: '+ self.first_name)
    
    def player_number(self):
        return('the '+ str(self.first_name)+ ' ' + str(self.last_name) + ' number is ' +str(self.number))


    
class Goalkeeper(Footbalist):
    pass


class Defenders(Footbalist):
    pass


player_1 = Footbalist('Mobin' , 'Yazdani' , 13 , 176 , 65)

player_2 = Goalkeeper('Milad' , 'Karimi' , 5 , 192 , 93)

player_6 = Defenders('Reza' , 'Afsordeh' , 1 , 177 , 26)


print(player_1.player_first_number())
print(player_1.player_number())