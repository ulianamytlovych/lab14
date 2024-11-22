class Teacher:
    def __init__(self, last_name, base_salary, experience):
        
        self.last_name = last_name
        self.base_salary = base_salary
        self.experience = experience

    def calculate_salary(self):
       
        if self.experience > 20:
            bonus = 0.15
        elif self.experience > 10:
            bonus = 0.10
        elif self.experience > 3:
            bonus = 0.05
        else:
            bonus = 0.0

        total_salary = self.base_salary * (1 + bonus)
        return total_salary

    def __str__(self):
    
        return f"Вчитель {self.last_name}, стаж: {self.experience} років, зарплата: {self.calculate_salary():.2f} грн."

teacher1 = Teacher("Іваненко", 15000, 5) 
teacher2 = Teacher("Петренко", 15000, 15)  
teacher3 = Teacher("Сидоренко", 15000, 25)  

print(teacher1)
print(teacher2)
print(teacher3)
