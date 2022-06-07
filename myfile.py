class Person():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def hello(self):
        print("Hello!")

    def report(self):
        print(f"I am {self.first_name} {self.last_name}")


class Agent(Person):

    def reveal(self, passcode):
        if passcode == 123:
            print("I am here!")
        else:
            self.report()


x = Agent("Binita", "Mandal")
x.report()
