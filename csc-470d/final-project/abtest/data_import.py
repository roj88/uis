import pandas as pd

class ImportData:
  def __init__(self, filename_dir):
        self.filename_dir = filename_dir

  def file_to_dataframe(filename_dir):
  	"""Reads a csv into a pandas dataframe

  	Args:
  		filename_dir (str): File name and directory

  	Returns:
  	A pandas dataframe of 
  	"""

  	df = pd.read_csv(filename_dir)

  	return df

