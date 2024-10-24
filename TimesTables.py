def multiples(table, startnum, endnum, pupilname):
	print(f"Hi {pupilname} ... here is your times table\n")
	for i in range(startnum, endnum+1): # upper range not inclusive
		print(f"{table} x {i} = {table * i}")

name = input("What is your name? ")
timesTable = int(input("Enter times table, start number and end number\n"))
startNumber = int(input(""))
endNumber = int(input(""))

multiples(timesTable, startNumber, endNumber, name)