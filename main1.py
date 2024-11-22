class Animal:
    def __init__(self, species, lifespan, offspring_per_year):
       
        self.species = species
        self.lifespan = lifespan
        self.offspring_per_year = offspring_per_year

    def calculate_offspring(self):
     
        if self.lifespan <= 3:
            return 0
        reproductive_years = self.lifespan - 3
        return reproductive_years * self.offspring_per_year

    def __str__(self):
       
        return f"Вид: {self.species}, Тривалість життя: {self.lifespan} років, Нащадки за життя: {self.calculate_offspring()}"


class DomesticAnimal(Animal):
    def __init__(self, species, lifespan, offspring_per_year, nickname):
        
        super().__init__(species, lifespan, offspring_per_year)
        self.nickname = nickname

    def calculate_offspring(self):
       
        if self.lifespan <= 3:
            return 0
        reproductive_years = self.lifespan - 3
        birth_years = reproductive_years // 2
        return birth_years * self.offspring_per_year

    def __str__(self):
       
        return f"Домашня тварина: {self.nickname} ({self.species}), Тривалість життя: {self.lifespan} років, Нащадки за життя: {self.calculate_offspring()}"



wild_animal = Animal("Вовк", 10, 5)  
domestic_animal = DomesticAnimal("Собака", 12, 4, "Баді")  

print(wild_animal)
print(domestic_animal)
