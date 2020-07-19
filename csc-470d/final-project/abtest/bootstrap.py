class Bootstrap:
  def __init__(self, dataframe):
        self.dataframe = dataframe
        self.bernoulli = bernoulli
        self.num_datasets = num_datasets
        self.control_treatment = control_treatment
        self.num_samples = num_samples


def bootstrap_monte_carlo(bernoulli, num_datasets, dataframe, control_treatment, num_samples=dataframe.size):
  """Performs bootstrap monte carlo on a pandas dataframe

  Args:
    bernoulli (bool): Whether the input data is a bernoulli or numeric output
    num_datasets (int): Number of aggregations to perform.
    dataframe (Panda Dataframe): Data frame with metrics.
    control_treatment (String; 'Treatment' or 'Control'): Treatment vs Control.
    metric (float): Metric name from dataframe.
    Optional: num_samples (int): Number of samples in each avg. Default is
                                dataframe.size.

  Returns:
    A list of boostrapped aggregations of len() num_datasets.
  """

  # array that will hold correlated data
  bootstrap_data_sets = []

  df = dataframe.loc[dataframe['control_treatment']==control_treatment]
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
    metric_total = 0
    successes_total = 0
    failures_total = 0

    # iterate through the number of samples
    for j in range(num_samples):
      # get random row numbers
      row_num = r.randint(0, data_frame_size - 1)

      if bernoulli:
        # append new samples to the data set
        successes_total += df['successes'].loc[row_num]
        trials_total += df['trials'].loc[row_num]

      else:
        # append new samples to the data set
        metric_total += df['metric'].loc[row_num]

    if bernoulli:
      # append boostrapped data sets
      bootstrap_data_sets.append(np.true_divide(successes_total, trials_total))
    else:
      # append boostrapped data sets
      bootstrap_data_sets.append(np.true_divide(metric_total, num_samples))


  print('Progress Complete!')

  return bootstrap_data_sets