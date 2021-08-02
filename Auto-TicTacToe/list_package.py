# Author: Rakshit Joshi
# Date of Creation: 26/06/2021
# Date of Last Modification: 27/06/2021

#returns reveresed value of the list provided
def reverse_list(lstVariable):
	try:
		new_reversed_list = []
		for list_element in lstVariable:
			new_reversed_list.insert(0,list_element)
		return new_reversed_list
	except:
		print("You can only reverse a 'list' with this function.")

#returns reveresed value of the string provided
def reverse_str(strVariable):
	try:
		strVariable+"c"
		list_of_string_char = list(strVariable)
		list_of_string_char
		element_removing_variable = 1
		for list_element in list_of_string_char:
			list_of_string_char.insert(0,list_element)
			list_of_string_char.pop(element_removing_variable)
			element_removing_variable=element_removing_variable+1
		reversed_string = ''.join(list_of_string_char)
		return reversed_string
	except:
		print("You can only reverse a 'string' with this function.")

#returns you a list of first 'n' even numbers
def n_even(first_n_even_numbers):
	try:
		even_list = []
		limit_of_range_of_even_numbers = first_n_even_numbers*2
		for even_number in range(0, limit_of_range_of_even_numbers, 2):
			even_list.append(even_number)
		return even_list
	except:
		print("You can only input an 'Integer'.")
		
#return you a list of first 'n' odd numbers
def n_odd(first_n_odd_numbers):
	try:
		odd_list = []
		limit_of_range_of_odd_numbers = first_n_odd_numbers*2
		for odd_number in range(1, limit_of_range_of_odd_numbers, 2):
			odd_list.append(odd_number)
		return odd_list
	except:
		print("You can only input an 'Integer'.")

#returns converted 'string type list' from 'integer type list':
def lst_intTOstr(intList):
	new_strList = []
	try:
		for intElements in intList:
			intElements+1-1
			new_strList.append(str(intElements))
		return new_strList
	except:
		print("You can only enter List with 'int' type elements.")

#returns converted 'integer type list' from 'string type list':
def lst_strTOint(strList):
	new_intList = []
	try:
		for strElements in strList:
			strElements+"c"
			new_intList.append(int(strElements))
		return new_intList
	except:
		print("You can only enter List with 'str' type elements.")

#returns edited (respected elements get deleted) list
def del_from(lstVariable, starting_index, total_elements, direction):
	try:
		if starting_index-total_elements>=-1:
			if direction == 1:
				new_deleted_element_list = []
				while total_elements > 0:
					temp_var = lstVariable.pop(starting_index)
					new_deleted_element_list.append(temp_var)
					total_elements = total_elements-1
				return new_deleted_element_list
			if direction == -1:
				new_deleted_element_list = []
				deleting_index = (starting_index-total_elements)+1
				while total_elements > 0:
					temp_var = lstVariable.pop(deleting_index)
					new_deleted_element_list.append(temp_var)
					total_elements = total_elements-1
				return new_deleted_element_list
		else:
			print("Total elements excceed the list.")
	except:
		print("Wrong Parameters.")

#returns edited (changing index of an element) list
def replace(target_list, target_index, new_index):
	new_edited_list = []
	try:
		target_element = target_list.pop(target_index)
		new_edited_list = target_list
		new_edited_list.insert(new_index, target_element)
		return new_edited_list
	except:
		print("Wrong Parameters.")

#returns the index of an element of a list
def indexOf(target_list, target_element):
	try:
		index = 0
		for temp_var in target_list:
			if temp_var != target_element and index<len(target_list)-1:
				index = index+1
				continue
			elif temp_var != target_element and index<=len(target_list):
				print("The element does not belong to the list.")
				index = (index-index)-1
				break
			else:
				break
		return index
	except:
	 	print("Wrong Parameters.")
