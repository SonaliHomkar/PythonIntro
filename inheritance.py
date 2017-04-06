class Parent():
    def __init__(self,last_name,eye_color):
        print("Parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name : " + self.last_name)
        print("Eye Color : " + self.eye_color)


class Child(Parent):
    def __init__(self,last_name,eye_color,number_of_toys):
        print("Child constructor called")
        Parent.__init__(self,last_name,eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        print("Last Name : " + self.last_name)
        print("Eye Color : " + self.eye_color)
        print("No of toys`: " + str(self.number_of_toys))
    

miley_cyrus = Child("Cyrus","blue",5)
#print(miley_cyrus.last_name)
#print(miley_cyrus.eye_color)
#print(miley_cyrus.number_of_toys)
miley_cyrus.show_info()
            
