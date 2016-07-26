done = False
number_list = []

#Prompt User to create array
print "*"*80
print "\nPlease enter a list of numbers between zero and some arbitrarily large value \n(inclusive). The list is in random order, but is guaranteed to contain one \n of every number in the range except one.\n"
print "*"*80
while done == False:
	cur =raw_input("Please Enter a Number (or 'done' to finish): ")
	if cur == 'done':
		done = True
	else:
		number_list.append(int(cur))

def find_missing_number(num_list):
	num_list.sort()
	found = False
	start = 0
	end = len(num_list) - 1
	#check end of list
	if num_list[end] == end:
		return end+1
	#check start of list
	if num_list[start] != start:
		return start

	while(start <= end and not found):
		mid = (end + start)/2
		if num_list[mid] > mid and num_list[(mid-1)] == (mid-1):
			found = True
		elif num_list[mid] > mid:
			end = mid - 1
		elif num_list[mid] == mid:
			start = mid + 1
	return mid

#most efficient algorithm
def find_missing_number1(num_list):
	#add numbers
	list_total = 0
	for i in num_list:
		list_total = list_total + i
	#figure out what it should be
	actual_total = len(num_list) * (len(num_list) + 1)/2
	#subtract
	return actual_total - list_total

print find_missing_number1(number_list)