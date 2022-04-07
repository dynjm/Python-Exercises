number = int(input())
romannumeral = []
newnum = ""

if number in range(1, 4000):
	if number >= 1000:
		thousand = number//1000
		romannumeral.append(thousand*"M")
		number += -(thousand * 1000)
		hundred = number//100
		if hundred == 9:
			romannumeral.append("CM")
		elif hundred == 4:
			romannumeral.append("CD")
		elif hundred >= 5:
			romannumeral.append("D")
			romannumeral.append((hundred-5)*"C")
		else:
			romannumeral.append(hundred*"C")
		number += -(hundred * 100)
		ten = number//10
		if ten == 9:
			romannumeral.append("XC")
		elif ten == 4:
			romannumeral.append("XL")
		elif ten >= 5:
			romannumeral.append("L")
			romannumeral.append((ten-5)*"X")
		else:
			romannumeral.append((ten)*"X")
		number += -(ten * 10)
		one = number//1
		if one == 9:
			romannumeral.append("IX")
		elif one == 4:
			romannumeral.append("IV")
		elif one >= 5:
			romannumeral.append("V")
			romannumeral.append((one-5)*"I")
		else:
			romannumeral.append((one)*"I")

	elif number >= 100:
		hundred = number//100
		if hundred == 9:
			romannumeral.append("CM")
		elif hundred == 4:
			romannumeral.append("CD")
		elif hundred >= 5:
			romannumeral.append("D")
			romannumeral.append((hundred-5)*"C")
		else:
			romannumeral.append(hundred*"C")
		number += -(hundred * 100)
		ten = number//10
		if ten == 9:
			romannumeral.append("XC")
		elif ten == 4:
			romannumeral.append("XL")
		elif ten >= 5:
			romannumeral.append("L")
			romannumeral.append((ten-5)*"X")
		else:
			romannumeral.append((ten)*"X")
		number += -(ten * 10)
		one = number//1
		if one == 9:
			romannumeral.append("IX")
		elif one == 4:
			romannumeral.append("IV")
		elif one >= 5:
			romannumeral.append("V")
			romannumeral.append((one-5)*"I")
		else:
			romannumeral.append((one)*"I")

	elif number >= 10:
		ten = number//10
		if ten == 9:
			romannumeral.append("XC")
		elif ten == 4:
			romannumeral.append("XL")
		elif ten >= 5:
			romannumeral.append("L")
			romannumeral.append((ten-5)*"X")
		else:
			romannumeral.append((ten)*"X")
		number += -(ten * 10)
		one = number//1
		if one == 9:
			romannumeral.append("IX")
		elif one == 4:
			romannumeral.append("IV")
		elif one >= 5:
			romannumeral.append("V")
			romannumeral.append((one-5)*"I")
		else:
			romannumeral.append((one)*"I")
		number += -(one * 1)

	elif number >= 1:
		one = number//1
		if one == 9:
			romannumeral.append("IX")
		elif one == 4:
			romannumeral.append("IV")
		elif one >= 5:
			romannumeral.append("V")
			romannumeral.append((one-5)*"I")
		else:
			romannumeral.append((one)*"I")
		
	while "" in romannumeral:
		romannumeral.remove("")

	print(newnum.join(romannumeral))



else:
	print("Invalid Input")