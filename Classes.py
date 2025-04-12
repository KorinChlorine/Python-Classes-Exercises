class Animals:
    def __init__(self, dogs):
        self.dogs = dogs

class Dog:
    def __init__(self, name, breed, age, size):
        self.name = name
        self.breed = breed
        self.age = age
        self.size = size

class DogManager:
    def __init__(self):
        self.dogs = []

    def add_dog(self, dog):
        self.dogs.append(dog)


key = "yes"
key2 = "yes"
while key == "yes":
    name, breed, age, size = "", "", "", ""
    dog = Dog(name, breed, age, size)
    dog_manager = DogManager()
    dog_manager.add_dog(dog)
    animal_instance = Animals(dog_manager.dogs)

    name = input("Enter dog name: ")
    breed = input("Enter dog breed: ")
    age = input("Enter dog age: ")
    size = input("Enter dog size: ")

    dog = Dog(name, breed, age, size)
    dog_manager.add_dog(dog)

    animal_instance = Animals(dog_manager.dogs)
    key = input("Successfully added dog! Add more (yes/no)?: ").lower()

    dog = Dog(name, breed, age, size)
    dog_manager = DogManager()
    dog_manager.add_dog(dog)
    print("-----\n")

    if key == "yes":
        continue
    else:
        key = "no"

while key2 == "yes":
    findName = input("Input dog's name to see characteristics: ")
    found = False
    for dog in dog_manager.dogs:
        if dog.name == findName:
            print("Dog found!")
            print("Name:", dog.name)
            print("Breed:", dog.breed)
            print("Age:", dog.age)
            print("Size:", dog.size)
            found = True
            break

    if not found:
        print("Dog not found.")
        print(dog_manager)

    ask = input("Continue? (yes/no) or add dog? (add): ").lower()
    if ask == "yes":
        continue
    else:
        key2 = "no"


class Genshin_Characters:
    def __init__(self, char):
        self.char = char


class Char_Detail:
    def __init__(self, name, vision, sex):
        self.name = name
        self.vision = vision
        self.sex = sex


def inputs():
    name = input("Input character name: ")
    vision = input("Input vision: ")
    sex = input("Input sex: ")
    cdInstance = Char_Detail(name, vision, sex)
    print(cdInstance.name, vision, sex)


inputs()

class Disorders:
    def __init__(self, fFour, sThree, tOne):
        self.fFour = fFour
        self.sThree = sThree
        self.tOne = tOne

class DisorderTypes(Disorders):
    def __init__(self, fFour, sThree, tOne, Trichotillomania, Pica, Anorexia, Bulimia, BodyDysmorphic, BingeEating):
        super().__init__(fFour, sThree, tOne)
        self.Trichotillomania = Trichotillomania
        self.Pica = Pica
        self.Anorexia = Anorexia
        self.Bulimia = Bulimia
        self.BodyDysmorphic = BodyDysmorphic
        self.BingeEating = BingeEating

def initialize_disorder_types():
    Trichotillomania = "Hair pulling when stressed"
    Pica = "Eating non-edible foods"
    Anorexia = "Does not eat at all"
    Bulimia = "Eats but will throw up later or will hunger himself/herself later"
    BodyDysmorphic = "Excessive comparison to other people's bodies or fear of being judged to their body"
    BingeEating = "Eats too much especially when stressed"
    return Trichotillomania, Pica, Anorexia, Bulimia, BodyDysmorphic, BingeEating


Trichotillomania, Pica, Anorexia, Bulimia, BodyDysmorphic, BingeEating = initialize_disorder_types()

disorder_instance = DisorderTypes("fFour_value", "sThree_value", "tOne_value",
                                  Trichotillomania, Pica, Anorexia, Bulimia, BodyDysmorphic, BingeEating)


class PC:
    def __init__(self, internalHW, externalHW):
        self.internalHW = internalHW
        self.externalHW = externalHW

    def displayIHW(self, motherboard = None, cpu = None, gpu = None):
        print("Motherboard:",motherboard)
        print("CPU:", cpu)
        print("GPU", gpu)

    def displayEHW(self, case = None, mouse = None, keyboard = None):
        print("Case:",case)
        print("Mouse:", mouse)
        print("Keyboard", keyboard)

class internalHW(PC):
    def __init__(self, motherboard, cpu, gpu):
        return

class externalHW(PC):
    def __init__(self, case, mouse, keyboard):
        return

internal = internalHW("GIGABYTE B450M DS3H V2","AMD Ryzen 2600", "NVIDIA GTX 1070")
external = externalHW("Inplay Meteor 01", "Rakk Lumanog", "Redragon Lakshimini")
internal.displayIHW()

class PC:
    def __init__(self, internalHW, externalHW):
        self.internalHW = internalHW
        self.externalHW = externalHW

    def displayIHW(self):
        print("Motherboard:", self.internalHW.motherboard)
        print("CPU:", self.internalHW.cpu)
        print("GPU:", self.internalHW.gpu)

    def displayEHW(self):
        print("Case:", self.externalHW.case)
        print("Mouse:", self.externalHW.mouse)
        print("Keyboard:", self.externalHW.keyboard)

class InternalHW:
    def __init__(self, motherboard, cpu, gpu):
        self.motherboard = motherboard
        self.cpu = cpu
        self.gpu = gpu

class ExternalHW:
    def __init__(self, case, mouse, keyboard):
        self.case = case
        self.mouse = mouse
        self.keyboard = keyboard

internal = InternalHW("GIGABYTE B450M DS3H V2", "AMD Ryzen 2600", "NVIDIA GTX 1070")
external = ExternalHW("Inplay Meteor 01", "Rakk Lumanog", "Redragon Lakshimini")

my_pc = PC(internal, external)
my_pc.displayIHW()
print("Case:", my_pc.externalHW.case)

class Job:
    tax = 0.20

class IT(Job):
    pass

class EmpStats:
    def calculateSal(self, salary, tax):
        add = 0
        deduc = salary * tax
        grossSal = salary - deduc
        if years >= 10:
            add = grossSal * 0.10
            grossSal += add
        return grossSal

    def displayStats(self, salary, tax):
        grossSal = self.calculateSal(salary, tax)
        print("\n\n\n\n\n")
        print("Name:", self.Name)
        print("ID:", self.ID)
        print("Years worked:", self.years)
        print("Tax:", tax)
        print("Gross Salary:", grossSal)

class regEmployee(EmpStats):
    def __init__(self, salary, ID, Name, years):
        self.tax = Job.tax
        self.salary = salary
        self.ID = ID
        self.Name = Name
        self.years = years

class conEmployee(EmpStats):
    def __init__(self, salary, ID, Name, years):
        self.tax = Job.tax + 0.20
        self.salary = salary
        self.ID = ID
        self.Name = Name
        self.years = years

def ask():
    salary = float(input("Salary: "))
    ID = input("ID: ")
    Name = input("Name: ")
    years = int(input("Years worked: "))
    return salary, ID, Name, years

selector = int(input("Enter 1 if you're a regular employee and 2 if a contractual employee: "))
if selector == 1:
    salary, ID, Name, years = ask()
    reg_emp = regEmployee(salary, ID, Name, years)
    reg_emp.displayStats(salary, reg_emp.tax)

elif selector == 2:
    salary, ID, Name, years = ask()
    con_emp = conEmployee(salary, ID, Name, years)
    con_emp.displayStats(salary, con_emp.tax)
else:
    print("Invalid")
