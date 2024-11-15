from dog import Dog
from guard_dog import GuardDog

my_dog = Dog()
my_dog.greet()
my_dog.be_friendly()
print()

my_guard_dog = GuardDog()
my_guard_dog.greet()
my_guard_dog.be_friendly()  # inherited method from Dog class
