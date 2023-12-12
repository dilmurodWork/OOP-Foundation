class Cat:

    def __init__(self, name: str = 'Kashak', age: int = 0, color: str = 'White', breed: str = "Simple"):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color

    def print_info(self):
        print(self.name, self.age, self.color, self.breed)

    def __str__(self):
        return f'{self.name.capitalize()} {self.age}'


boris = Cat('Ninja', 3)
boris.print_info()
print(boris)

