import bootstrap as bs
import data_import as di
import errors
import statistical_tests as st
import random
import pandas as pd
import matplotlib.pyplot as plt
import args
import sys
import os
import seaborn as sns


if __name__ == '__main__':
	# parse arguments from CLI
	argument_dict = vars(args.get_options(sys.argv[1:]))

	argument_dict['bernoulli'] = argument_dict['type'].lower()=='bernoulli'

	# raise set of parsing errors
	errors.parsing_errors(argument_dict)
	
	# show user arguments
	i = 1 # set number
	print('Below are the arguments in this test:')
	for key in argument_dict:
		print(" {}.) {}: {}".format(i, key, argument_dict[key]))
		i += 1

	# import data frame
	dataframe = di.file_to_dataframe(argument_dict['file_name'])

	# raise dataframe import errors
	errors.df_import_errors(dataframe, argument_dict)

	# perform statistical tests, binomial ones if bernouli and numerical otherwise
	if argument_dict['bernoulli']==True:
		br = st.bernoulli_rate(dataframe)
		print("\nBelow is the bernoulli rate dataframe:")
		print(br)

		binomial_test = st.binomial_test(dataframe, argument_dict['alpha'])
		print("\nBelow is the result of the binomial test:")
		print(binomial_test)

	else:
		nm = st.numerical_mean(dataframe)
		print("\nBelow is the numerical mean dataframe:")
		print(nm)

		t_test = st.t_test(dataframe)
		print("\nBelow is the result of the t-test:")
		print(t_test)


	# create variable to hold control and treatment bootstraps
	# this is important to make sure that we are calculating confidence intervals
	# the same bootstraps we are visualizing
	x = {}
	for tc in ['control', 'treatment']:
		x[tc] = bs.bootstrap_monte_carlo(dataframe, tc, num_datasets=1000)

	# calculate confidence intervals
	df_confidence_intervals = pd.DataFrame()
	for tc in ['control', 'treatment']:
		ci = bs.confidence_intervals(x[tc], tc)
		df_confidence_intervals = df_confidence_intervals.append(pd.DataFrame(ci))

	print("\nBelow are the confidence intervals:")
	print(df_confidence_intervals)

	
	# for loop to iterate through experimentation groups
	for tc in ['control', 'treatment']:
		# set solors
		if tc == 'control':
			color = '#1f77b4'
		elif tc == 'treatment':
			color = '#ff7f0e'

		# create scalars for CIs
		a = df_confidence_intervals['lower_bound'].loc[df_confidence_intervals['control_treatment']==tc].sum()
		b = df_confidence_intervals['median'].loc[df_confidence_intervals['control_treatment']==tc].sum()
		c = df_confidence_intervals['upper_bound'].loc[df_confidence_intervals['control_treatment']==tc].sum()

		# add lines for confidence intervals
		plt.axvline(a, label=tc+" lower_bound", linestyle='--', dashes=(5, 1), color = color)
		plt.axvline(b, label=tc+" median", linestyle='--', dashes=(5, 5), color = color)
		plt.axvline(c, label=tc+" upper_bound", linestyle='--', dashes=(5, 10), color = color)
		
		# add in distributions
		sns.distplot(x[tc], label=tc, color = color)

		# add legend and labels
		plt.legend(loc='best')
		plt.xlabel('Test Metric')
		plt.ylabel('Density')
		plt.title('A/B Test Bootstrap Comparisons')

	# show vizualization
	plt.show()




