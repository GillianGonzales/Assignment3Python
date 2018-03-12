#
# Created By GIllian
# Created On March 11 2018
#
# This program will calculate the price of pizza

# The menu 
print ("These are the prices for toppings:")
print ("1 topping is 1$")
print ("2 toppings is 1.75$")
print ("3 toppings is 2.50$")
print ("4 toppings is 3.35$")
print ("")
print ("These prices for the sizes are:")
print ("Large is 6$")
print ("ExtraLarge is 10$")
print ("")

# Making Instructions
topping = input("Type the price topping you want: ")
size = input("Type in the size.Type in the integer for size = ExtraLarge is 0, Large is 1 : ")

#Assigning variables
topping1 = "1"
topping2 = "2"
topping3 = "3"
topping4 = "4"
HTS = 0.13
Large = "1"
ExtraLarge = "0"


# The funtion that will calculate the price of the the pizza
if topping + size == topping1 + Large:
	#Reassigning Variable
	Large = 6
	#Calculating Subtotal
	print ("This is the subtotal")
	input(float(Large) + float(topping1))
	#Calculating Taxees
	print("The taxes are ")
	input((float(Large) + float(topping1)) * float(HTS))
	#Calculating total cost
	print("This is the total cost")
	input((float(Large) + float(topping1)) * float(HTS) + float(Large) + float(topping1))
	#Reassigning Variable Back
	Large = "1"
	pass

if topping + size == topping2 + Large:
	#Reassigning Variables
	topping2 = 1.75
	Large = 6
	#Calculating Subtotal
	print ("This is the subtotal")
	input(float(Large) + float(topping2))
	print("The taxes are ")
	#Calculating Taxees
	input((float(Large) + float(topping2)) * float(HTS))
	#Calculating total cost
	print("This is the total cost")
	input((float(Large) + float(topping2)) * float(HTS) + float(Large) + float(topping2))
	#Reassigning Variables Back
	topping2 = "2"
	Large = "1"
	pass

if topping + size == topping3 + Large:
	#Reassigning Variables
	topping3 = 2.50
	Large = 6
	#Calculating Subtotal
	print ("This is the subtotal")
	input(float(Large) + float(topping3))
	#Calculating Taxees
	print("The taxes are ")
	input((float(Large) + float(topping3)) * float(HTS))
	#Calculating total cost
	print("This is the total cost")
	input((float(Large) + float(topping3)) * float(HTS) + float(Large) + float(topping3))
	#Reassigning Variables Back
	topping3 = "3"
	Large = "1"
	pass

if topping + size == topping4 + Large:
	#Reassigning Variables
	topping4 = 3.35
	Large = 6
	#Calculating Subtotal
	print ("This is the subtotal")
	input(float(Large) + float(topping4))
	#Calculating Taxees
	print("The taxes are ")
	input((float(Large) + float(topping4)) * float(HTS))
	#Calculating total cost
	print("This is the total cost")
	input((float(Large) + float(topping4)) * float(HTS) + float(Large) + float(topping4))
	#Reassigning Variables Back
	topping4 = "4"
	Large = "1"
	pass

if topping + size == topping1 + ExtraLarge:
	#Reassigning Variable
	ExtraLarge = 10
	#Calculating Subtotal
	print ("This is the subtotal")
	input(float(ExtraLarge) + float(topping1))
	#Calculating Taxees
	print("The taxes are ")
	input((float(ExtraLarge) + float(topping1)) * float(HTS))
	#Calculating total cost
	print("This is the total cost")
	input((float(ExtraLarge) + float(topping1)) * float(HTS) + float(ExtraLarge) + float(topping1))
	#Reassigning Variable Back
	ExtraLarge = "0"
	pass

if topping + size == topping2 + ExtraLarge:
	#Reassigning Variables
	topping2 = 1.75
	ExtraLarge = 10
	#Calculating Subtotal
	print ("This is the subtotal")
	input(float(ExtraLarge) + float(topping2))
	#Calculating Taxees
	print("The taxes are ")
	input((float(ExtraLarge) + float(topping2)) * float(HTS))
	#Calculating total cost
	print("This is the total cost")
	input((float(ExtraLarge) + float(topping2)) * float(HTS) + float(ExtraLarge) + float(topping2))
	#Reassigning Variables Back
	topping2 = "2"
	ExtraLarge = "0"
	pass

if topping + size == topping3 + ExtraLarge:
	#Reassigning Variables
	topping3 = 2.50
	ExtraLarge = 10
	#Calculating Subtotal
	print ("This is the subtotal")
	input(float(ExtraLarge) + float(topping3))
	#Calculating Taxees
	print("The taxes are ")
	input((float(ExtraLarge) + float(topping3)) * float(HTS))
	#Calculating total cost
	print("This is the total cost")
	input((float(ExtraLarge) + float(topping3)) * float(HTS) + float(ExtraLarge) + float(topping3))
	#Reassigning Variables Back
	topping3 = "3"
	ExtraLarge = "0"
	pass

if topping + size == topping4 + ExtraLarge:
	#Reassigning Variables
	topping4 = 3.35
	ExtraLarge = 10
	#Calculating Subtotal
	print ("This is the subtotal")
	input(float(ExtraLarge) + float(topping4))
	#Calculating Taxees
	print("The taxes are ")
	input((float(ExtraLarge) + float(topping4)) * float(HTS))
	#Calculating total cost
	print("This is the total cost")
	input((float(ExtraLarge) + float(topping4)) * float(HTS) + float(ExtraLarge) + float(topping4))
	#Reassigning Variables Back
	topping4 = "4"
	ExtraLarge = "0"
	pass

print("")
input("end program")