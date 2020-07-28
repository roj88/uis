import sys
import os


def parsing_errors(argument_dict):
	"""
	Raise errors from parsing the system args.

	Args:
		argument_dict (dict): Dict of parsed system commands.

	Returns:
		Nothing.
	"""
	# raise error if sys parser has too few arguments
	if len(argument_dict) < 5:
		raise Exception('Too few CLI arguments!')
		sys.exit(0)

	# raise error if sys parser has too many arguments
	if len(argument_dict) > 5:
		raise Exception('Too many CLI arguments!')
		sys.exit(0)

	# raise error if file does not exist
	if not(os.path.exists(argument_dict['file_name'])):
		raise Exception('File does not exist.')
		sys.exit(0)

	# raise error if power and alpha are outside of 0 and 1
	if not(0 < argument_dict['power'] < 1) or  not(0 < argument_dict['alpha'] < 1):
		raise Exception('Please enter a value between 0 and 1 (not inclusive) for power and/or alpha.')
		sys.exit(0)


def df_import_errors(df, argument_dict):
	"""
	Raise errors from parsing the system args.

	Args:
		df (Panda Dataframe): Data frame with metrics.
	argument_dict (dict): Dict of parsed system commands.

	Returns:
		Nothing.
	"""
	# raise error if the df doesn't have metrics and control_treatment fields
	if not('metric' in list(df.columns)) or not('control_treatment' in list(df.columns)):
		raise Exception('Please add a dataframe with the fields metric and control_treatment.')
		sys.exit(0)

	# raise error if metric is not numerical and control_treatment is not a string
	if not(df['control_treatment'].dtypes=='object') or not(df['metric'].dtypes=='int64' or df['metric'].dtypes=='float64'):
		raise Exception('Please add a dataframe with a numeric metric values and string control_treatment values.')
		sys.exit(0)

	# raise error if the df doesn't have data
	if len(df)==0:
		raise Exception('Empty csv added.')
		sys.exit(0)

	# raise error if the df is numerical but the option is bernoulli
	metric_values = list(df['metric'].unique())
	metric_values.sort()
	if argument_dict['type']=='bernoulli' and metric_values != [0,1]:
		raise Exception('Data set is not just 0s and 1s, and thus not binomial.')
		sys.exit(0)

	# raise error if there are more group names than just treatment and control
	tc_values = list(df['control_treatment'].unique())
	tc_values.sort()
	if tc_values != ['control', 'treatment']:
		raise Exception('Only control and treatment should be present in control_treatment field.')
		sys.exit(0)

	# raise error if the df is numerical but the option is bernoulli
	metric_values = list(df['metric'].unique())
	metric_values.sort()
	if argument_dict['type']=='numeric' and metric_values == [0,1]:
		raise Exception('Data set is just 0s and 1s, but numeric was chosen.')
		sys.exit(0)
