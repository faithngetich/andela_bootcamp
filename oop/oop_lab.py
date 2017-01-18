class Car:
	def __init__(self):
		self.doors = 4

    def get_doors(self):
    	print(self.doors)

#Ferrari inherits from Car
 class Ferrari((Cars)):
 	def __init__(self):
 		self.doors = 2

#data in the Car and Ferrari class is encapsulated in the peugot and ferrari object
Peugot = Car()
Ferrari = Ferrari()

#Polymorphism.
#we are able to call the .get_doors on a ferrari object because Ferrari is a subclass of car
peugot.get_doors()
ferrari.get_doors()


