
# No other modules apart from 'csv' need to be imported
# as they aren't required to solve the assignment

# Import required module/s
import csv

def readScoreSheet(file_name):
	"""Reads the input CSV file of Score Sheet and creates a mapping of student name with his/her marks.

	Parameters
	----------
	file_name : str
		CSV file name of Score Sheet

	Returns
	-------
	dict
		Mapping of each student's name and his/her marks as { Key : Value } pair
	
	Example
	-------
	>>> csv_file_name = 'week4_assignment2_sample.csv'
	>>> print( readScoreSheet( csv_file_name ) )
	{
		'Harv': 20.0, 'Virge': 52.0, 'Teresita': 93.0, 'Maire': 9.0, 'Jenica': 57.0, 'Kermie': 32.0, 'Chelsie': 11.0, 
		'Emilio': 95.0, 'Wynne': 14.0, 'Kelley': 66.0
	}
	"""

	name_score_mapping = {}
	input_file_obj = open(file_name, 'r')
	
	##############	ADD YOUR CODE HERE	##############
	reader=csv.reader(input_file_obj)
	next(reader)
	for line in reader:
		name_score_mapping[line[0]] =float(line[1])
	#name_score_mapping = dict(list(name_score_mapping.items())[1:])
	 	 

	##################################################
	
	input_file_obj.close()

	return name_score_mapping


def getTheTopper(mapping_dict):
	"""Get the name of student with maximum score in the given mapping of student and their scores.
	
	Parameters
	----------
	mapping_dict : dict
		Mapping of each student's name and his/her marks as { Key : Value } pair

	Returns
	-------
	str
		Name of student with maximum score
	
	Example
	-------
	>>> name_score_mapping = {
								'Harv': 20.0, 'Virge': 52.0, 'Teresita': 93.0, 'Maire': 9.0, 'Jenica': 57.0, 'Kermie': 32.0, 
								'Chelsie': 11.0, 'Emilio': 95.0, 'Wynne': 14.0, 'Kelley': 66.0
							}
	>>> print( getTheTopper( name_score_mapping ) )
	'Emilio'
	"""

	name_with_max_score = ''

	##############	ADD YOUR CODE HERE	##############
	value=list(mapping_dict.values())
	key=list(mapping_dict.keys())	
	position=value.index(max(value))
	name_with_max_score=key[position]	

	##################################################

	return name_with_max_score


if __name__ == "__main__":
	"""Main function, code begins here.
	"""
	csv_file_name = 'week4_assignment2_sample.csv'
	name_score_mapping = readScoreSheet(csv_file_name)
	print(name_score_mapping)
	topper_name = getTheTopper(name_score_mapping)
	print(topper_name)
