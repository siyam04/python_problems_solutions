def BinarySearch(List, item):

	Start = 0
	End = len(List) - 1
	Found = False

	while (Found == False and Start <= End):
		Mid = (Start + End) // 2

		if (List[Mid] == item):
			Found = True
			return Found
		elif (List[Mid] < item):
			Start = Mid + 1
		else:
			End = Mid - 1
	return Found

List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

item = int(input("Which Item You want to Find?\n"))

if (BinarySearch(List, item)):
	print(item, "is Found")
else:
	print(item, "is NOT Found")



