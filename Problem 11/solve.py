#!/usr/bin/python

import sys

#Max and Min index of rows and columns
row_max, col_max = 19, 19
row_min, col_min = 0, 0
adjacent = 4
products = []

def left(row, col):
	prod = 1
	for i in range(col, col-adjacent, -1):
		if (i >= col_min and i <= col_max):
			prod *= int(grid[row][i])
		else:
			return False
	return prod

def right(row, col):
	prod = 1
	for i in range(col, col+adjacent, 1):
		if (i >= col_min and i <= col_max):
			prod *= int(grid[row][i])
		else:
			return False
	return prod

def up(row, col):
	prod = 1
	for i in range(row, row-adjacent, -1):
		if (i >= row_min and i <= row_max):
			prod *= int(grid[i][col])
		else:
			return False
	return prod

def down(row, col):
	prod = 1
	for i in range(row, row+adjacent, 1):
		if (i >= row_min and i <= row_max):
			prod *= int(grid[i][col])
		else:
			return False
	return prod

def diagonal_down_right(row,col):
	prod = 1
	for i in range(1, 5, 1):
		temp_row = row + i
		temp_col = col + i
		if (temp_row >= row_min and temp_row <= row_max and temp_col >= col_min and temp_col <= col_max):
			prod *= int(grid[temp_row][temp_col])
		else:
			return False
	return prod

def diagonal_down_left(row,col):
	prod = 1
	for i in range(1, 5, 1):
		temp_row = row + i
		temp_col = col - i
		if (temp_row >= row_min and temp_row <= row_max and temp_col >= col_min and temp_col <= col_max):
			prod *= int(grid[temp_row][temp_col])
		else:
			return False
	return prod

def diagonal_up_right(row,col):
	prod = 1
	for i in range(1, 5, 1):
		temp_row = row - i
		temp_col = col + i
		if (temp_row >= row_min and temp_row <= row_max and temp_col >= col_min and temp_col <= col_max):
			prod *= int(grid[temp_row][temp_col])
		else:
			return False
	return prod

def diagonal_up_left(row,col):
	prod = 1
	for i in range(1, 5, 1):
		temp_row = row - i
		temp_col = col - i
		if (temp_row >= row_min and temp_row <= row_max and temp_col >= col_min and temp_col <= col_max):
			prod *= int(grid[temp_row][temp_col])
		else:
			return False
	return prod

fp = open(sys.argv[1],"r");
grid = []
data = fp.read()
fp.close()
rows = data.split("\n")
for row in rows:
	grid.append(row.split(" "))

for row in range(0,row_max+1, 1):
	for col in range(0, col_max+1, 1):
		values = []
		values.append(left(row,col))
		values.append(right(row,col))
		values.append(up(row,col))
		values.append(down(row,col))
		values.append(diagonal_down_right(row,col))
		values.append(diagonal_down_left(row,col))
		values.append(diagonal_up_right(row,col))
		values.append(diagonal_up_left(row,col))
		temp_max = max(values);
		products.append(temp_max)
		print("(" + str(row) +"," + str(col) +") = " + str(temp_max))

print("Requred value = " + str(max(products)))
