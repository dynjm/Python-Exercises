temp = input().split()
r = int(temp[0])
c = int(temp[1])
words = []
grid = []
for a in range(r):
	grid.append(input())

N = int(input())
for b in range(N):
	words.append(input())

def checkhorizontal(word,grid,row,col,r,c):
	number = col
	if c-col < len(word):
		pass
	else:
		col += 1
		for letter in range(1, len(word)):
			if word[letter] == grid[row][col]:
				if letter == len(word)-1:
					return True
				else:
					col += 1
					continue
			else:
				col = number
				break
	
	if c-(c-col)+1 < len(word):
		return False
	col += -1
	for letter in range(1, len(word)):
		if word[letter] == grid[row][col]:
			if letter == len(word)-1:
				return True
			else:
				col += -1
				continue
		else:
			col = number
			return False

def checkvertical(word,grid,row,col,r,c):
	number = row
	if r-row < len(word):
		pass
	else:
		row += 1
		for letter in range(1, len(word)):
			if word[letter] == grid[row][col]:
				if letter == len(word)-1:
					return True
				else:
					row += 1
					continue
			else:
				row = number
				break

	if r-(r-row)+1 < len(word):
		return False
	row += -1
	for letter in range(1, len(word)):
		if word[letter] == grid[row][col]:
			if letter == len(word)-1:
				return True
			else:
				row += -1
				continue
		else:
			row = number
			return False

def checkdiagonal(word,grid,row,col,r,c):
	number1 = row
	number2 = col
	#northeast
	if c-col >= len(word) and r-(r-row)+1 >= len(word):
		col += 1
		row += -1
		for letter in range(1, len(word)):
			if word[letter] == grid[row][col]:
				if letter == len(word)-1:
					return True
				else:
					col += 1
					row += -1
					continue
			else:
				col = number2
				row = number1
				break
	#southeast
	if r-row >= len(word) and c-col >= len(word):
		col += 1
		row += 1
		for letter in range(1, len(word)):
			if word[letter] == grid[row][col]:
				if letter == len(word)-1:
					return True
				else:
					col += 1
					row += 1
					continue
			else:
				col = number2
				row = number1
				break
	#southwest
	if r-row >= len(word) and c-(c-col)+1 >= len(word):
		col += -1
		row += 1
		for letter in range(1, len(word)):
			if word[letter] == grid[row][col]:
				if letter == len(word)-1:
					return True
				else:
					col += -1
					row += 1
					continue
			else:
				col = number2
				row = number1
				break
	#northwest
	if r-(r-row)+1 >= len(word) and c-(c-col)+1 >= len(word):
		col += -1
		row += -1
		for letter in range(1, len(word)):
			if word[letter] == grid[row][col]:
				if letter == len(word)-1:
					return True
				else:
					col += -1
					row += -1
					continue
			else:
				col = number2
				row = number1
				return False

	return False

for word in words:
	
	row = 0
	col = 0
	firstletter = (0, 0)
	while r > row:
		if c > col:
			
			if grid[row][col] == word[0]:
				firstletter = (row+1, col+1)
				if len(word) == 1:
					print(int(firstletter[0]), end=" ")
					print(int(firstletter[1]))
					break
				if checkhorizontal(word,grid,row,col,r,c) == True:
					print(int(firstletter[0]), end=" ")
					print(int(firstletter[1]))
					break
				if checkvertical(word,grid,row,col,r,c) == True:
					print(int(firstletter[0]), end=" ")
					print(int(firstletter[1]))
					break
				if checkdiagonal(word,grid,row,col,r,c) == True:
					print(int(firstletter[0]), end=" ")
					print(int(firstletter[1]))
					break
				else:
					row = firstletter[0]-1
					col = firstletter[1]
					continue

			col += 1
			continue
		else:
			col = 0
			row += 1