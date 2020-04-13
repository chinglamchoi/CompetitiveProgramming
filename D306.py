# a = input()
# hostt = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', '-']
# usernamee = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', '+']

# if a.count("@") > 1:
# 	print("Invalid")
# else:
# 	if ("@" not in a) or (a[0] == "@") or (a[len(a)-1] == "@"):
# 		print("Invalid")
# 	else:
# 		z = a.find("@")
# 		c = a[:z]
# 		d = a[z+1:]
# 		lengthoc = len(c)
# 		lengthod = len(d)
# 		lenu = len(usernamee)
# 		lenh = len(hostt)
# 		if (c.find("..") != -1) or (c[0] == ".") or (c[lengthoc-1] == ".") or (d.find("..") != -1) or (d.find(".") == -1) or (d.find("-.") != -1) or (d.find(".-") != -1) or (d[0] == ".") or (d[lengthoc-1] == "."):
# 			print("Invalid")
# 		else:
# 			count = 0
# 			check = True
# 			if lengthoc > lenu:
# 				for i in range(0, lenu):
# 					if (i == (lenu - 1)) and (usernamee[i] not in c):
# 						check = False
# 						print("Invalid")
# 						break
# 					if usernamee[i] in c:
# 						break
# 			else:
# 				for i in range(0, lengthoc):
# 					if (i == (lengthoc - 1)) and (c[i] not in usernamee):
# 						check = False
# 						print("Invalid")
# 						break
# 					if c[i] in usernamee:
# 						break			
# 			if check == True:
# 				d = list(d)
# 				d.remove(".")
# 				d = "".join(d)
# 				count = 0
# 				if lengthod > lenh:
# 					for i in range(0, lenh):
# 						if (i == (lenh - 1)) and (hostt[i] not in d):
# 							check = False
# 							print("Invalid")
# 							break
# 						if hostt[i] in d:
# 							count = count + 1
# 						if count == 2:
# 							check = True
# 							break
# 				else:
# 					for i in range(0, lengthod):
# 						if (i == (lengthod - 1)) and (d[i] not in hostt):
# 							check = False
# 							print("Invalid")
# 							break
# 						if d[i] in hostt:
# 							count = count + 1
# 						if count == 2:
# 							check = True
# 							break

# 	try:
# 		if check == True:
# 			print("Valid")
# 	except NameError:
# 		pass



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
		lenu = len(usernamee)
		lenh = len(hostt)
		if (c.find("..") != -1) or (c[0] == ".") or (c[lengthoc-1] == ".") or (d.find("..") != -1) or (d.find(".") == -1) or (d.find("-.") != -1) or (d.find(".-") != -1) or (d[0] == ".") or (d[lengthoc-1] == "."):
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

	try:
		if check == True:
			print("Valid")
	except NameError:
		pass
