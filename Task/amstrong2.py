def Amstrong (x,y):
	for i in range (x,y):
		j = i
		total = 0
		while (j>0):
			reminder = j%10
			total = total + (reminder**3)
			j = j/10
		if i==total : print i
a = int (input ("enter the staring number of amstrong"))
b = int (input ("enter the finishing number of Amstrong"))
Amstrong (a,b)