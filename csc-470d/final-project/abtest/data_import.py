import pandas as pd
import sys

def file_to_dataframe(filename_dir):
	"""Reads a csv into a pandas dataframe

	Args:
		filename_dir (str): File name and directory

	Returns:
		A pandas dataframe from the file. 
	"""
	try:
		df = pd.read_csv(filename_dir)

	except:
		raise Exception("Error importing csv.")
		sys.exit(0)

	return df

