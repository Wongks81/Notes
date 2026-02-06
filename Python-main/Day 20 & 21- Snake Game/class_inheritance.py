class Animal:
    def __init__(self):
        self.num_eyes = 2
    
    def breathe(self):
        print("Inhale, exhale.")

# Fish is inheriting Animal class
class Fish(Animal):
    def __init__(self):
        # this super refers to the super or parent class that the current class is inheriting
        # call to super() in init is reccomended but not required
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Underwater")

    # Overwrite the properties from the super / parent class
    def mutate_eyes(self):
        self.num_eyes = 4

    def swim(self):
        print("moving in water")

nemo = Fish()
nemo.swim()
nemo.breathe()
nemo.mutate_eyes()
print(nemo.num_eyes)