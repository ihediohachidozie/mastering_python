class Parent:
    hair_color = "brown"
    speaks = ["English"]

class Child(Parent):
    hair_color = "purple"
    def __init__(self):
        super().__init__()
        self.speaks.append("German")

print(Child.speaks)
little_one = Child()

print(little_one.speaks)