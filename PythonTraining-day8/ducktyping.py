'''
    Duck typing:
        Duck typing is a concept related to dynamic typing,
        where the type or the class of an object is less important than the methods it defines.
        When you use duck typing, you do not check types at all.
        Instead, you check for the presence of a given method or attribute.
    Duck Typing comes from the phrase:
        “If it looks like a duck and quacks like a duck, it’s a duck”
'''
class duck:
    def sound(self):
        print("Quack Quack")
class dog:
    def sound(self):
        print("Bow Bow")
class cat:
    def sound(self):
        print("Meow Meow")
def all_sound(obj):
    obj.sound()
animal=cat()
all_sound(animal)

