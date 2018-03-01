class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name - " + self.last_name)
        print("Eye Color - "+ self.eye_color)

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child constructor called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

eric_holmen = Parent("Holmen","Brown")
eric_holmen.show_info()
griffin_holmen = Child("Holmen","Grey","1000")
griffin_holmen.show_info()
#print(griffin_holmen.last_name)
#print(griffin_holmen.number_of_toys)
#print(eric_holmen.last_name)
