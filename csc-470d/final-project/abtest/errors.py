import sys
import os

def parsing_errors(argument_dict):
	# set series of parsing errors
	if len(argument_dict) < 5:
		raise Exception('Too few CLI arguments!')
		sys.exit(0)

	if len(argument_dict) > 5:
		raise Exception('Too many CLI arguments!')
		sys.exit(0)

	if not(os.path.exists(argument_dict['file_name'])):
		raise Exception('File does not exist.')
		sys.exit(0)

	if not(isinstance(argument_dict['bernoulli'], bool)):
		raise Exception('Please enter a bool for the bernoulli option.')
		sys.exit(0)

	if not(0 < argument_dict['power'] < 1) or  not(0 < argument_dict['alpha'] < 1):
		raise Exception('Please enter a value between 0 and 1 (not inclusive) for power and/or alpha.')
		sys.exit(0)

def df_import_errors(df, argument_dict):
	# set series of parsing errors
	if not('metric' in list(df.columns)) or not('control_treatment' in list(df.columns)):
		raise Exception('Please add a dataframe with the fields metric and control_treatment.')
		sys.exit(0)

	# set series of parsing errors
	if argument_dict['bernoulli']==True and not(list(df['metric'].unique()).sort() == [0,1]):
		raise Exception('Data set is not just 0s and 1s, and thus not binomial.')
		sys.exit(0)
