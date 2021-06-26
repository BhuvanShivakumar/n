def diff(price, N, M): #keep finding the difference between the elements
    #price.sort()
# Variable Declaration
	prev = 999999 
	minimum = 0
	high = 0
	low = 0
	
	print("Here the goodies that are selected for distribution are: \n")
	for i in range(N-M+1):
		minimum = min(prev, price[i+M-1][1] - price[i][1])
		if minimum < prev:
			high = i+M-1
			low = i
		prev = minimum
		
	return high, low, minimum

items = {}
#extracting input file
with open("goodie.txt") as f:
    for line in f:
       (key, val) = line.split(": ")
       items[key] = int(val)	   
#print(items)
#price = list(items.values())
sort_items = sorted(items.items(), key = lambda x:x[1])

#No of Goodies
N = len(items)
#print(N)

#No of employees
M = int(input("Enter no. of employee: \n"))
#print(no_of_employee)

high, low, minDiff = diff(sort_items, N, M)

for i in range(low,high+1):
	print(sort_items[i])

print("\nAnd the difference between the chosen goodie with highest price and the lowest price is :", minDiff)
Enter no. of employee: 
8
Here the goodies that are selected for distribution are: 

('MI Band', 999)
('Sandwich Toaster', 2195)
('Cult Pass', 2799)
('Scale', 4999)
('Fitbit Plus', 7980)
('Microwave Oven', 9800)
('Alexa', 9999)
('Digital Camera', 11101)

And the difference between the chosen goodie with highest price and the lowest price is : 10102
