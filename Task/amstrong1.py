for i in range (1,1000):
	j = i
	total = 0
	while (j>0):
		reminder = j%10
		total = total + (reminder**3)
		j = j/10
	if i==total : print i