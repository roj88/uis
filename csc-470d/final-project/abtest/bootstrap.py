import pandas as pd
import numpy as np
import math
import random as r


def bootstrap_monte_carlo(df, control_treatment, num_samples=None, num_datasets=None):
  """
  Performs bootstrap monte carlo on a pandas dataframe

  Args:
    df (Panda Dataframe): Data frame with metrics.
    control_treatment (String; 'Treatment' or 'Control'): Treatment vs Control.
    Optional:
      num_samples (int): Number of samples in each avg. Default is len(dataframe).
      num_datasets (int): Number of samples in each aggregation. Default is 1000.

  Returns:
    A list of boostrapped aggregations of len() num_datasets.
  """
  # inform user of bootstrap beginning
  print("Beginning bootstrap process!")

  # Create conditions for num_datasets option
  if num_datasets is None:
    num_datasets=1000

  # array that will hold correlated data
  bootstrap_data_sets = []

  # create df of control/treatment data
  df = df.loc[df['control_treatment']==control_treatment]
  df.reset_index(drop=True, inplace=True)

  # Create conditions for num_samples option
  if num_samples is None:
    num_samples=len(df)

  # gets the size of the data set to prevent out of bounds errors
  data_frame_size = len(df.index)

  # create status bar
  increments = math.ceil(num_datasets/5)

  # iterate through number of data sets
  for i in range(num_datasets):
    # print out status message
    if i%increments==0:
      print("{}% done".format(100*i/num_datasets))
    
    # define search and omnibox_counts
    metric_total = 0

    # iterate through the number of samples
    for j in range(num_samples):
      # get random row numbers
      row_num = r.randint(0, data_frame_size - 1)

      # append new samples to the data set
      metric_total += df['metric'].loc[row_num]

    # append boostrapped data sets
    bootstrap_data_sets.append(np.true_divide(metric_total, num_samples))

  print('Progress Complete!')

  return bootstrap_data_sets


def confidence_intervals(bootstrap_data_sets, control_treatment=None):
  """
  Calculates bootstrap confidence intervals from a list of bootstrap aggs.
  Specifically from the output of bootstrap_monte_carlo(),

  Args:
    bootstrap_data_sets (list): A list of boostrapped aggregations.
    control_treatment (str): Whether this data is control or treatment..

  Returns:
    A list of dict of confidence intervals.
  """
  # calculate the lower and upper bound of a 95% confidence interval and
  # calculate medians
  p_lower_bound = np.percentile(bootstrap_data_sets, 2.5)
  p_median = np.percentile(bootstrap_data_sets, 50)
  p_upper_bound = np.percentile(bootstrap_data_sets, 97.5)

  # place calculations in dict and return dict
  ci_dict = {'control_treatment': [control_treatment], 'lower_bound': [p_lower_bound], 'median': [p_median], 'upper_bound': [p_upper_bound]}

  return ci_dict


