# class Employee:
#     def __init__(self, name: str, salary: float):
#         self.name = name
#         self.salary = salary
#     def raise_salary(self, parcent: float):
#         increase = self.salary * (parcent / 100)
#     def get_info(self):
#         return f"Nome: {self.name}; Salário: {self.salary:.2f}"

# funcionario1 = Employee("João", 5000.0)
# print(funcionario1.get_info())

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def raise_salary(self, percent):
        increase_amount = self.salary * percent / 100
        self.salary += increase_amount

    def get_info(self):
        return f"Nome: {self.name}; Salário: {self.salary:.2f}"

# Criando objetos Employee
funcionario1 = Employee("John Doe", 50000.0)
funcionario2 = Employee("Jane Smith", 65000.0)

# Imprimindo informações iniciais
print("Informações iniciais:")
print(funcionario1.get_info())
print(funcionario2.get_info())
print()

# Dando aumento de 10% para ambos os funcionários
funcionario1.raise_salary(10)
funcionario2.raise_salary(10)

# Imprimindo informações atualizadas
print("Informações após aumento de salário:")
print(funcionario1.get_info())
print(funcionario2.get_info())