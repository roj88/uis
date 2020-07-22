import pandas as pd

def file_to_dataframe(filename_dir):
	"""Reads a csv into a pandas dataframe

	Args:
		filename_dir (str): File name and directory

	Returns:
	A pandas dataframe of 
	"""
	df = pd.read_csv(filename_dir)

	return df

