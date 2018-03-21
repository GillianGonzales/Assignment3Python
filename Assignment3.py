#
# Created By GIllian
# Created On March 11 2018
#
# This program will calculate the price of pizza

# The menu 
print ("These are the prices for toppings:")
print ("1 topping is $1")
print ("2 toppings is $1.75")
print ("3 toppings is $2.50")
print ("4 toppings is $3.35")
print ("")
print ("These prices for the sizes are:")
print ("Large is $6")
print ("ExtraLarge is $10")
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
	topping1SubL = float(Large) + float(topping1)
	topping1SubLFormat = '${:,.2f}'.format(topping1SubL)
	input(topping1SubLFormat)
	#Calculating Taxees
	print("The taxes are ")
	topping1TaxL = (float(Large) + float(topping1)) * float(HTS)
	topping1TaxLFormat = '${:.2f}'.format(topping1TaxL)
	input(topping1TaxLFormat)
	#Calculating total cost
	print("This is the total cost")
	topping1TotalL = (float(Large) + float(topping1)) * float(HTS) + float(Large) + float(topping1)
	topping1TotalLFormat = '${:,.2f}'.format(topping1TotalL)
	input(topping1TotalLFormat)
	#Reassigning Variable Back
	Large = "1"
	pass

if topping + size == topping2 + Large:
	#Reassigning Variables
	topping2 = 1.75
	Large = 6
	#Calculating Subtotal
	print ("This is the subtotal")
	topping2SubL = float(Large) + float(topping2)
	topping2SubLFormat = '${:,.2f}'.format(topping2SubL)
	input(topping2SubLFormat)
	#Calculating Taxees
	print("The taxes are ")
	topping2TaxL = (float(Large) + float(topping2)) * float(HTS)
	topping2TaxLFormat = '${:.2f}'.format(topping2TaxL)
	input(topping2TaxLFormat)
	#Calculating total cost
	print("This is the total cost")
	topping2TotalL = (float(Large) + float(topping2)) * float(HTS) + float(Large) + float(topping2)
	topping2TotalLFormat = '${:,.2f}'.format(topping2TotalL)
	input(topping2TotalLFormat)
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
	topping3SubL = float(Large) + float(topping3)
	topping3SubLFormat = '${:,.2f}'.format(topping3SubL)
	input(topping3SubLFormat)
	#Calculating Taxees
	print("The taxes are ")
	topping3TaxL = (float(Large) + float(topping3)) * float(HTS)
	topping3TaxLFormat = '${:,.2f}'.format(topping3TaxL)
	input(topping3TaxLFormat)
	#Calculating total cost
	print("This is the total cost")
	topping3TotalL = (float(Large) + float(topping3)) * float(HTS) + float(Large) + float(topping3)
	topping3TotalLFormat = '${:,.2f}'.format(topping3TotalL)
	input(topping3TotalLFormat)
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
	topping4SubL = float(Large) + float(topping4)
	topping4SubLFormat = '${:,.2f}'.format(topping4SubL)
	input(topping4SubLFormat)
	#Calculating Taxees
	print("The taxes are ")
	topping4TaxL = (float(Large) + float(topping4)) * float(HTS)
	topping4TaxLFormat = '${:,.2f}'.format(topping4TaxL)
	input(topping4TaxLFormat)
	#Calculating total cost
	print("This is the total cost")
	topping4TotalL = (float(Large) + float(topping4)) * float(HTS) + float(Large) + float(topping4)
	topping4TotalLFormat = '${:,.2f}'.format(topping4TotalL)
	input(topping4TotalLFormat)
	#Reassigning Variables Back
	topping4 = "4"
	Large = "1"
	pass

if topping + size == topping1 + ExtraLarge:
	#Reassigning Variable
	ExtraLarge = 10
	#Calculating Subtotal
	print ("This is the subtotal")
	topping1SubEX = float(ExtraLarge) + float(topping1)
	topping1SubEXFormat = '${:,.2f}'.format(topping1SubEX)
	input(topping1SubEXFormat)
	#Calculating Taxees
	print("The taxes are ")
	topping1TaxeEX = (float(ExtraLarge) + float(topping1)) * float(HTS)
	topping1TaxeEXFormat = '${:,.2f}'.format(topping1TaxeEX)
	input(topping1TaxeEXFormat)
	#Calculating total cost
	print("This is the total cost")
	topping1TotalEX = (float(ExtraLarge) + float(topping1)) * float(HTS) + float(ExtraLarge) + float(topping1)
	topping1TotalEXFormat = '${:,.2f}'.format(topping1TotalEX)
	input(topping1TotalEXFormat)
	#Reassigning Variable Back
	ExtraLarge = "0"
	pass

if topping + size == topping2 + ExtraLarge:
	#Reassigning Variables
	topping2 = 1.75
	ExtraLarge = 10
	#Calculating Subtotal
	print ("This is the subtotal")
	topping2SubEX = float(ExtraLarge) + float(topping2)
	topping2SubEXFormat = '${:,.2f}'.format(topping2SubEX)
	input(topping2SubEXFormat)
	#Calculating Taxees
	print("The taxes are ")
	topping2TaxeEX = (float(ExtraLarge) + float(topping2)) * float(HTS)
	topping2TaxeEXFormat = '${:,.2f}'.format(topping2TaxeEX)
	input(topping2TaxeEXFormat)
	#Calculating total cost
	print("This is the total cost")
	topping2TotalEX = (float(ExtraLarge) + float(topping2)) * float(HTS) + float(ExtraLarge) + float(topping2)
	topping2TotalEXFormat = '${:,.2f}'.format(topping2TotalEX)
	input(topping2TotalEXFormat)
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
	topping3SubEX = float(ExtraLarge) + float(topping3)
	topping3SubEXFormat = '${:,.2f}'.format(topping3SubEX)
	input(topping3SubEXFormat)
	#Calculating Taxees
	print("The taxes are ")
	topping3TaxeEX = (float(ExtraLarge) + float(topping3)) * float(HTS)
	topping3TaxeEXFormat = '${:,.2f}'.format(topping3TaxeEX)
	input(topping3TaxeEXFormat)
	#Calculating total cost
	print("This is the total cost")
	topping3TotalEX = (float(ExtraLarge) + float(topping3)) * float(HTS) + float(ExtraLarge) + float(topping3)
	topping3TotalEXFormat = '${:,.2f}'.format(topping3TotalEX)
	input(topping3TotalEXFormat)
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
	topping4SubEX = float(ExtraLarge) + float(topping4)
	topping4SubEXFormat = '${:,.2f}'.format(topping4SubEX)
	input(topping4SubEXFormat)
	#Calculating Taxees
	print("The taxes are ")
	topping4TaxEX = (float(ExtraLarge) + float(topping4)) * float(HTS)
	topping4TaxEXFormat = '${:,.2f}'.format(topping4TaxEX)
	input(topping4TaxEXFormat)
	#Calculating total cost
	print("This is the total cost")
	topping4TotalEX = (float(ExtraLarge) + float(topping4)) * float(HTS) + float(ExtraLarge) + float(topping4)
	topping4TotalEXFormat = '${:,.2f}'.format(topping4TotalEX)
	input(topping4TotalEXFormat)
	#Reassigning Variables Back
	topping4 = "4"
	ExtraLarge = "0"
	pass

print("")
input("end program")