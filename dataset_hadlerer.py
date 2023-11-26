import validate


class Adress():
    def __init__(self, zipcode, city, street, number) -> None:
        self.zipcode = zipcode
        self.city = city
        self.street = street
        self.bnumber = number
    

class Plant():
    def __init__(self, x, y, t) -> None:
        self.x = x
        self.y = x
        self.ty = t # the type of the tree (currently only graphical)

    def move(self, nx, ny):
        self.x = nx     #new x position
        self.y = ny     #new y position



class Profil():
    def __init__(self, e_adress, usr_name, r_adress: Adress) -> None:
        self.e_adress = e_adress
        self.usr_name = usr_name
        self.r_adress: Adress = r_adress
        self.drops = 0
        self.plants = []


    def plant_plant(self, x, y, t):
        self.plants.append(Plant(x, y, t))
    
    


class City():
    def __init__(self, name, population, long, lat) -> None:
        self.name = name
        self.population = population
        self.plants = 0
        self.longitude = long
        self.latitude = lat


class World():
    def __init__(self):
        self.name_to_city = {}
        self.e_adress_to_city = {}
        self.e_adress_to_person = {}
    
    def add_city(self, name, pop, long, lat):
        if not name in self.names_to_cityes.keys(): 
            self.name_to_city[name] = City(name, pop, long, lat) # register city
        
    def add_usr(self, e_adress, usr_name, r_adress):
        if not e_adress in self.e_adress_to_person.keys():
            p = Profil(e_adress, usr_name, r_adress)  # register user
            self.e_adress_to_person[e_adress] = p
            self.e_adress_to_city[e_adress] = self.name_to_city[p.r_adress.city]
        else:
            pass
            #redirect to log in

    def add_drops(self, e_address, to_validate, amount):
        if (validate.Validate(to_validate)):
            self.e_adress_to_person[e_address].drops += amount

    def add_plant(self, e_adress, x, y, t):
        if (self.e_adress_to_person[e_adress].drops > 15):
            self.e_adress_to_person[e_adress].plant_plant(x, y, t)
            self.e_adress_to_person[e_adress].drops -= 15
            self.e_adress_to_city[e_adress].plants += 1
    

    def get_usr_data(self, e_adress):
        return(self.e_adress_to_person[e_adress])
    
    def get_city_data(self, name):
        return(self.name_to_city[name])