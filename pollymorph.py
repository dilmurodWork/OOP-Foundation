class Student:
    def __init__(self,
                 name: str, age: int,
                 sex: str, car: bool,
                 course: int, scholarship: float):
        self.name = name
        self.age = age
        self.sex = sex
        self.car = car
        self.course = course
        self.scholarship = scholarship

    def __str__(self):
        return self.name + ' ' + str(self.age)

    def __int__(self):
        return self.age + 1

    def __len__(self):
        return len(self.name)

    def __getitem__(self, key):
        if key == 'name':
            return self.name
        elif key == 'age':
            return self.age
        elif key == 'sex':
            return self.sex
        elif key == 'car':
            return self.car
        elif key == 'course':
            return self.course
        elif key == 'scholarship':
            return self.scholarship
        else:
            raise KeyError(f'Invalid key: {key}')

    def __setitem__(self, key, value):
        if key == 'name':
            self.name = value
        elif key == 'age':
            self.age = value
        elif key == 'sex':
            self.sex = value
        elif key == 'car':
            self.car = value
        elif key == 'course':
            self.course = value
        elif key == 'scholarship':
            self.scholarship = value
        else:
            raise KeyError(f'Invalid key: {key}')

    def __delitem__(self, key):
        if key == 'name':
            del self.name
        elif key == 'age':
            del self.age
        elif key == 'sex':
            del self.sex
        elif key == 'car':
            del self.car
        elif key == 'course':
            del self.course
        elif key == 'scholarship':
            del self.scholarship
        else:
            raise KeyError(f'Invalid key: {key}')

    def __eq__(self, other):
        return self.age == other.age

    def __gt__(self, other):
        return self.age > other.age

    def __lt__(self, other):
        return self.age < other.age

    def __ge__(self, other):
        return self.age >= other.age

    def __le__(self, other):
        return self.age <= other.age

    def __ne__(self, other):
        return self.age != other.age

    def __add__(self, other):
        return self.scholarship + other.scholarship

    def __sub__(self, other):
        return self.scholarship - other.scholarship

    def __mul__(self, other):
        return self.scholarship * other.scholarship


anna = Student('Anna', 17, 'F', False, 1, 149.99)
bob = Student('Bob', 19, 'M', True, 3, 49.99)

print(anna == bob)
print(anna > bob)
print(anna < bob)
print(anna >= bob)
print(anna <= bob)
print(anna - bob)
print(dir(Student))