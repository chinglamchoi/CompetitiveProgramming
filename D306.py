a = input()
hostt = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', '-']
usernamee = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', '+']

if a.count("@") > 1:
	print("Invalid")
else:
	if ("@" not in a) or (a[0] == "@") or (a[len(a)-1] == "@"):
		print("Invalid")
	else:
		z = a.find("@")
		c = a[:z]
		d = a[z+1:]
		lengthoc = len(c)
		lengthod = len(d)
		if (c.find("..") != -1) or (c[0] == ".") or (c[lengthoc-1] == ".") or (d.find("..") != -1) or (d.find(".") == -1) or (d.find("-.") != -1) or (d.find(".-") != -1) or (d[0] == ".") or (d[lengthod-1] == "."):
			print("Invalid")
		else:
			count = 0
			check = True
			for i in range(0, lengthoc):
				if (i == (lengthoc - 1)) and (c[i] not in usernamee):
					check = False
					print("Invalid")
					break
				if c[i] in usernamee:
					break			
			if check == True:
				d = list(d)
				d.remove(".")
				d = "".join(d)
				count = 0
				for i in range(0, lengthod):
					if (i == (lengthod - 1)) and (d[i] not in hostt):
						check = False
						print("Invalid")
						break
					if d[i] in hostt:
						count = count + 1
					if count == 2:
						check = True
						break
			if check == True:
				for i in c:
					if i not in usernamee:
						print("Invalid")
						check = False
			if check == True:
				for i in d:
					if i not in hostt:
						print("Invalid")
						check = False
	try:
		if check == True:
			print("Valid")
	except NameError:
		pass
