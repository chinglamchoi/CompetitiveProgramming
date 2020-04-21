for i in range(10):
	a,b = input().split(" ")
	valid = 1
	if a == "OCT": #the input given is in octal
		c = "DEC "
		try:
			b = int(b, 8) #yes it is an octal
			if (b > 32) or (b < 1): #mvoe outside try? do I need to change the logic operators
				valid = 0
			else:
				c = c + str(b)
		except ValueError:
			valid = 0
	else: #number is given in decimal
		c = "OCT "
		try:
			b = int(b) # yes it is a decimal
			b = str(oct(b)).replace("0o", "")
			e = [str(i) for i in range(1, 32)]
			if b not in e:
				valid = 0
			else:
				c = c + b
		except ValueError:
			valid = 0
		

	if valid == 0:
		print("No solution")
	else:
		if len(c) < 6:
			c = c[:4] + "0" + c[-1]
		print(c)
