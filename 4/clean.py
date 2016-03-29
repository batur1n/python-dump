def clean_list(list_to_clean):
	new_list = []
	for i in list_to_clean:
		if not i in new_list:
			new_list.append(i)
		elif isinstance(i, float):
			new_list.append(i)
	return new_list

print(clean_list([1, 1.0, '1', -1, 1]))
print(clean_list(['qwe', 'reg', 'qwe', 'REG']))
print(clean_list([32, 32.1, 32.0, -123]))
print(clean_list([1, 2, 1, 1, 3, 4, 5, 4, 6, '2', 7, 8, 9, 0, 1, 2, 3, 4, 5]))
