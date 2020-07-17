class Bootstrap:
  


def bootstrap_monte_carlo_numeric(num_datasets, dataframe, pre_post, metric, num_samples=dataframe.size):
  """Performs bootstrap monte carlo.

  Performs bootstrap monte carlo on data from the table
  rjcarter.duet_analysis_pre_post

  Args:
    num_datasets (int): Number of aggregations to perform.
    dataframe (Panda Dataframe): Data frame with pre_post and metric totals.
    pre_post (String; 'Pre' or 'Post'): Pre-period vs post-period.
    metric (float): Metric name from dataframe.
    Optional: num_samples (int): Number of samples in each avg. Default is
                                dataframe.size.

  Returns:
    A list of boostrapped aggregations of len() num_datasets.
  """

  # array that will hold correlated data
  bootstrap_data_sets = []

  df = dataframe.loc[dataframe['pre_post']==pre_post]
  df.reset_index(drop=True, inplace=True)

  # gets the size of the data set to prevent out of bounds errors
  data_frame_size = len(df.index)

  # create status bar
  increments = math.ceil(num_datasets/20)

  # iterate through number of data sets
  for i in range(num_datasets):
    # print out status message
    if i%increments==0:
      print("{}% done".format(100*i/num_datasets))
    # define search and omnibox_counts
    total = 0

    # iterate through the number of samples
    for j in range(num_samples):
      # get random row numbers
      row_num = r.randint(0, data_frame_size - 1)

      # append new samples to the data set
      total += df[metric].loc[row_num]

    # append boostrapped data sets
    bootstrap_data_sets.append(np.true_divide(total, num_samples))

  print('Progress Complete!')

  return bootstrap_data_sets