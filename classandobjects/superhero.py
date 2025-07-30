# Avenger class
class Avenger:
    def __init__(self, name, age, gender, super_power, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon

    def get_info(self):
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Gender     : {self.gender}")
        print(f"Superpower : {self.super_power}")
        print(f"Weapon     : {self.weapon}")
        print("-----------------------------")

    def is_leader(self):
       
        if self.name == "Captain America":
            print(f"{self.name} is the leader of the Avengers.\n")
        else:
            print(f"{self.name} is not the leader of the Avengers.\n")


# Creating the superheroes
super_heroes = {
    "Captain America": {"age": 100, "gender": "Male", "super_power": "Super Strength", "weapon": "Shield"},
    "Iron Man": {"age": 48, "gender": "Male", "super_power": "Technology", "weapon": "Armor"},
    "Black Widow": {"age": 35, "gender": "Female", "super_power": "Superhuman", "weapon": "Batons"},
    "Hulk": {"age": 40, "gender": "Male", "super_power": "Unlimited Strength", "weapon": "No Weapon"},
    "Thor": {"age": 1500, "gender": "Male", "super_power": "Super Energy", "weapon": "Mjölnir"},
    "Hawkeye": {"age": 38, "gender": "Male", "super_power": "Fighting Skills", "weapon": "Bow and Arrows"},
}

avenger_team = []
for name, details in super_heroes.items():
    hero = Avenger(name, details["age"], details["gender"], details["super_power"], details["weapon"])
    avenger_team.append(hero)

# Display all Avengers info and leadership status
for hero in avenger_team:
    hero.get_info()
    hero.is_leader()
