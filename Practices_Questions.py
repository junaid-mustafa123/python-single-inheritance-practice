#***************************************************
# 1️⃣ Employee → Manager
# Parent (Employee):
# name
# salary
# show_details()
# Child (Manager):
# department
# show_manager_info()
# ✔ Make object → show both methods.
#***************************************************


class Employee:
    def __init__(self,name,salary,dept):
        self.name=name
        self.salary=salary
        self.dept=dept

    def show_detail(self):
        print("--------EMPLOYEE DETAILS -----------")
        print(f"NAME :{self.name}")
        print(f"SARLARY :{self.salary}")
        print(f"DEPARTMENT : {self.dept}")
        print("--------------------------------------")

class Manager(Employee):

    def show_manager_info(self):
        print("-----------MANAGER DETAILS ------")
        print(f"MANAGER NAME : {self.name}")
        print(f"DEPARTMENT : {self.dept}")
        print("----------------------------------")


obj=Manager("junaid",2000,"Computer Science")
obj.show_detail()
obj.show_manager_info()        




#***********************************
# 2️⃣ Vehicle → Car
# Parent (Vehicle):
# brand
# start()
# Child (Car):
# model
# drive()
# ✔ Car object → both functions run.
#***********************************


class Vechicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def start(self):
        print("--------BRAND DETAIL---------")
        print(f"CAR IS START")
        print(f"BRAND NAME : {self.brand}")
        print("----------------------------")

class Car(Vechicle):
    def drive(self):
        print("---------CAR DETAIL ---------")
        print(f"DRIVER IN CAR ")
        print(f"Brand Model : {self.brand}")
        print(f"MODEL : {self.model}")
        print("------------------------------")

obj = Car("TOYOTA","2025")  
obj.start()
obj.drive()
    

#****************************************
# 3️⃣ Person → Student
# Parent (Person):
# name
# age
# introduce()
# Child (Student):
# roll_no
# study()
# ✔ Student object → introduce() + study()
#****************************************



class Student:
    def __init__(self,name,age,roll_no):
        self.name=name
        self.age=age
        self.roll_no=roll_no

    def introduction(self):
        print("-----INTRODUCTION  DETAIL----------")  
        print(f"NAME :{self.name}")
        print(f"AGE : {self.age}")  
        print("-----------------------------------")
        
class Child(Student):

    def study(self):
        print("------STUDY DETAIL---------")
        print(f"NAME : {self.name}")
        print(f"ROLL NO : {self.roll_no}")
        print("-----------------------------")


obj=Child('JUNAID',19,'24SW53')
obj.introduction()
obj.study()

    

#****************************************
# 4️⃣ Product → Laptop
# Parent (Product):
# name
# price
# show_product()
# Child (Laptop):
# ram
# show_specs()
# ✔ Laptop object → all details show
#****************************************


class Product:
    def __init__(self,name,price,ram):
        self.name=name
        self.price=price
        self.ram=ram

    def show_product(self):
        print("----------PRODUCT DETAILS----------")    
        print(f"NAME : {self.name}")
        print(f"PRICE : {self.price}")
        print("------------------------------------")
        
class Laptop(Product):
    def show_specs(self):
        print("----------LAPTOP DETAILS ----------")
        print(f"NAME : {self.name}")
        print(f"RAM : {self.ram}")
        print("------------------------------------")


obj=Laptop('HP',55000,'8GB')
obj.show_product()
obj.show_specs()        