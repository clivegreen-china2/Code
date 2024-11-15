from dog import Dog


class GuardDog(Dog):

    def __init__(self, sound="Grrrr!"):
        super().__init__(sound)

    def greet(self):
        print(self.greeting, ' ... Who are you?')
