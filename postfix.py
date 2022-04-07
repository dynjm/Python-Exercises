stack = []
infix = []
operators = ["+", "-", "*", "/"]

expression = input().split()

for x in expression:
	if x not in operators:
		stack.append(int(x))
		infix.append(str(x))
		print(stack)
	else:
		if 2 > len(stack):
			print("Invalid expression.")
			infix.append("Invalid expression.")
			break
		else:
			operand2 = stack.pop()
			operand1 = stack.pop()
			if x == "+":
				stack.append(int(operand1 + operand2))
				if 2 > len(infix):
					infix.append("(" + str(operand1) + " + " + str(operand2) + ")")
				else:
					operand4 = infix.pop()
					operand3 = infix.pop()
					infix.append("(" + operand3 + " + " + operand4 + ")")

			elif x == "-":
				stack.append(int(operand1 - operand2))
				if 2 > len(infix):
					infix.append("(" + str(operand1) + " - " + str(operand2) + ")")
				else:
					operand4 = infix.pop()
					operand3 = infix.pop()
					infix.append("(" + operand3 + " - " + operand4 + ")")

			elif x == "*":
				stack.append(int(operand1*operand2))
				if 2 > len(infix):
					infix.append("(" + str(operand1) + " * " + str(operand2) + ")")
				else:
					operand4 = infix.pop()
					operand3 = infix.pop()
					infix.append("(" + operand3 + " * " + operand4 + ")")

			else:
				stack.append(int(operand1//operand2))
				if 2 > len(infix):
					infix.append("(" + str(operand1) + " / " + str(operand2) + ")")
				else:
					operand4 = infix.pop()
					operand3 = infix.pop()
					infix.append("(" + operand3 + " / " + operand4 + ")")

			print(stack)

if infix[-1] != "Invalid expression.":
	if len(infix) > 1:
		print("Invalid expression.")
	else:
		infix.append(" = " + str(stack[0]))
		output = ""
		print(output.join(infix))