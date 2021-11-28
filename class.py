class em:
    increment = 10
    em_no = 0

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        em.em_no = em.em_no + 1

    def increase(self):
        self.salary = self.salary + em.increment

    @classmethod
    def fromstr(cls, em_string):
        name, age, salary = em_string.split('-')
        return cls(name, age, salary)

    @staticmethod
    def greeting():
        return 'hello! welcome to office'


bikram = em('bikram', 22, 100)
bibek = em('bibek', 18, 20)
bishal = em.fromstr('bishal-20-80')

print(bikram.__dict__)
print(em.__dict__)

print(bibek.salary)
bibek.increase()
print(bikram.name, bibek.salary)
print(bikram.em_no)

a = em.greeting()
print(a)

print(f'age of bishal {bishal.age}.')


# dunder methods:: magic fn
# __add__, repr, str,
# __mul__   .....ect
