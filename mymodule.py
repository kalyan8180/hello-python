age = 20 #global variable
 
def display(): #simple function in python with no return and no argument
      print ("Welcome to my module")

class Info(): # class in python
      company = "Infosys" #class variables
      location = "Blore" #class variables


      def information (self): # method inside a class, so self needs to be arg
            print (self.company, self.location)
            #since accessing a class variable use self in front of them
