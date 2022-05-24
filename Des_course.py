"""object oriented programming"""

d1 = ["Designer", "Philip"]


class SoftwareEngineer:
    alias = "D3stinn3"

    def __init__(self, name, age, level, salary):
        # instance arguments or attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    def code(self):
        print(f"{self.name} is writing code...")
        if self.name == 'Destinne':
            print("this must be {} on the {}".format('Destinne', 'decks'))
        else:
            print("this must not be {}".format('destinny'))

    def code_in_language(self, language):
        # the 'language' is instance or argument defined in the class Software engineer through code_in_language
        print(f"{self.name} is writing code in {language}")


se1 = SoftwareEngineer("Destinne", 20, "Junior", 5000)
print(se1.name, se1.alias)
se1.code()
se1.code_in_language("python")
