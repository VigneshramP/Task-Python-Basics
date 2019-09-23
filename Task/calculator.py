def Addition ():
	c = a +b
	print "The Addition of Two Numbers is :" 
	print c

def Subtraction ():
	c = a - b
	print "The Subtraction of Two Numbers is :" 
	print c

def Division ():
	if (a>b):
		c = a / b
		print "The Division of Two Numbers is: "
		print c
	else :
		c = b/a
		print "The Division of Two Number is :"
		print c

def Modulus ():
	if (a>b):
		c = a % b
		print "The Modulus of Two Numbers is : "
		print c
	else :
		c = b%a
		print "The Modulus of Two Number is :"
		print c
def Factorial (x,y) :
	fact=1
	while(x>0):
		fact = fact*x
		x = x-1
	print "The Factorial Value of First Number :",fact
	fact1 = 1
	while(y>0 ):
		fact1 = y*fact1
		y-=1		
	print "The Factorial Value of Second Number :",fact1
	
a = int (input (" Enter the Value of First Number:"))
b = int (input ( "Enter the Value of Second Number:"))

chooise = int (input("1.Addition" 
		   "2.Subtraction"
		   "3.Division"
		   "4.Modulus"
		   "5.Factorial"))

if (chooise == 1 ):
	Addition ()
	pass

elif (chooise == 2 ):
	Subtraction()
	pass

elif (chooise == 3) :
	Division()
	pass

elif (chooise == 4) :
	Modulus()
	pass

elif(chooise == 5) :
	Factorial(a,b)
	pass

else:
	print "Please Enter The Correct Value"