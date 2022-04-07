def converttohindu(number):

	romannumeral = number

	romannumdict = {
	"I":1,
	"V":5,
	"X":10,
	"L":50,
	"C":100,
	"D":500,
	"M":1000
	}

	answer = 0

	convert = [x for x in romannumeral]

	count = 0
	i = len(romannumeral) - 1
	while i >= 0:
		if  i != len(romannumeral) - 1:
			if romannumdict[convert[i+1]] > romannumdict[convert[i]]:
				answer += -romannumdict[convert[i]]
			else:
				answer += romannumdict[convert[i]]
			count += 1
			i += -1
		else:
			answer += romannumdict[convert[i]]
			i += -1
			count += 1

	return answer

print(converttohindu(input()))