def find_max_min(list_of_input_numbers):
	#max and min return maximum and minimum numbers in an array respectively
  if max(list_of_input_numbers) == min(list_of_input_numbers):
    return [max(list_of_input_numbers)]#returns one value if all numbers are the same
  else:
    # returns minimum and maxinimum numbers in array respectively
    return [min(list_of_input_numbers), max(list_of_input_numbers)]