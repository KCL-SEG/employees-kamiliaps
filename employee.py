"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract_type, commission_state):
        self.name = name
        self.contract_type = contract_type
        self.commission_state = commission_state
        self.num_of_hours = 0
        self.wage = 0
        self.salary = 0
        self.num_of_contracts = 0
        self.commission_rate = 0
        self.commission = 0
        self.total_pay = 0

    def calculate_pay(self):
        if (self.contract_type == "salary") and (self.commission_state == False):
            self.total_pay = self.salary
        elif (self.contract_type == "hourly") and (self.commission_state == False):
            self.total_pay = self.wage * self.num_of_hours
        elif (self.contract_type == "salary") and (self.commission_state == True) and (self.num_of_contracts == 0):
            self.total_pay = self.salary + self.commission
        elif (self.contract_type == "hourly") and (self.commission_state) == True and (self.num_of_contracts == 0):
            self.total_pay = (self.wage * self.num_of_hours) + self.commission
        elif (self.contract_type == "salary") and (self.commission_state == True) and (self.num_of_contracts > 0):
            self.total_pay = self.salary + (self.num_of_contracts * self.commission_rate)
        elif (self.contract_type == "hourly") and (self.commission_state == True) and (self.num_of_contracts > 0):
            self.total_pay = (self.wage * self.num_of_hours) + (self.num_of_contracts * self.commission_rate)
    

    def get_salary(self):
        return self.salary

    def get_pay(self):
        return self.total_pay

    def __str__(self):
        if (self.contract_type == "salary") and (self.commission_state == False):
            return(f'{self.name} works on a monthly salary of {self.salary}. Their total pay is {self.total_pay}.')
        elif (self.contract_type == "hourly") and (self.commission_state == False):
            return(f'{self.name} works on a contract of {self.num_of_hours} at {self.wage}/hour. Their total pay is {self.total_pay}.')
        elif (self.contract_type == "salary") and (self.commission_state == True) and (self.num_of_contracts == 0):
            return(f'{self.name} works on a monthly salary of {self.salary} and receives a bonus commission commission of {self.commission}. Their total pay is {self.total_pay}.')
        elif (self.contract_type == "hourly") and (self.commission_state == True) and (self.num_of_contracts == 0):
            return(f'{self.name} works on a contract of {self.num_of_hours} at {self.wage}/hour and receives a bonus commission commission of {self.commission}. Their total pay is {self.total_pay}')
        elif (self.contract_type == "salary") and (self.commission_state == True) and (self.num_of_contracts > 0):
            return(f'{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.num_of_contracts} contract(s) at {self.commission_rate}/contract. Their total pay is {self.total_pay}.')
        elif (self.contract_type == "hourly") and (self.commission_state == True) and (self.num_of_contracts > 0):
            return(f'{self.name} works on a contract of {self.num_of_hours} at {self.wage}/hour and receives a commission for {self.num_of_contracts} contract(s) at {self.commission_rate}/contract. Their total pay is {self.total_pay}.')
        else:
            return("Error")


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 'salary', False)
billie.salary = 4000
billie.calculate_pay()

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 'hourly', False)
charlie.num_of_hours = 100
charlie.wage = 25
charlie.calculate_pay()

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 'salary', True)
renee.salary = 3000
renee.num_of_contracts = 4
renee.commission_rate = 200
renee.calculate_pay()

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 'hourly', True)
jan.num_of_hours = 150
jan.wage = 25
jan.num_of_contracts = 3
jan.commission_rate = 220
jan.calculate_pay()

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 'salary', True)
robbie.salary = 2000
robbie.commission = 1500
robbie.num_of_contracts = 0
robbie.calculate_pay()

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 'hourly', True)
ariel.num_of_hours = 120
ariel.wage = 30
ariel.commission = 600
ariel.calculate_pay()
