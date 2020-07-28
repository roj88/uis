import scipy.stats as stats
import pandas as pd
import numpy as np


def numerical_mean(df):
    """
    Calculates the means of the control and treatment data sets.

    Args:
        df (Panda Dataframe): Data frame with metrics.

    Returns:
        A pd.Dataframe with group means.
    """
    # create list of means
    control_treatment_data  = [
        df['metric'].loc[df['control_treatment'] == 'control'].mean(),
            df['metric'].loc[df['control_treatment'] == 'treatment'].mean()]
    # make dict to later be placed in df
    d = {'control_treatment': ['control','treatment'], 'avg': control_treatment_data}
    dataframe = pd.DataFrame(data=d)
    
    # return data frame of means
    return dataframe


def t_test(df):
    """
    Performs a t-test on a data set.

    Args:
        df (Panda Dataframe): Data frame with metrics.

    Returns:
        Tuple of t-statistic and p-value.
    """
    # place control and treatment data in seperate series
    a = df['metric'].loc[df['control_treatment'] == 'control']
    b = df['metric'].loc[df['control_treatment'] == 'treatment']
    
    # run t-test
    t2, p2 = stats.ttest_ind(a,b)

    # return tuple with t-test and p_value
    return t2, p2


def bernoulli_rate(df):
    """
    Calulates probabilities from bernoulli dataset.

    Args:
        df (Panda Dataframe): Data frame with metrics.

    Returns:
        A pd.Dataframe with group rates/probabilities.
    """
    # create pivot data of 
    summary = df.pivot_table(values='metric', index='control_treatment', aggfunc=np.mean)
    summary['metric'] = summary['metric']/summary['metric'].sum()

    # return summary table
    return summary


def binomial_test(df, p_value):
    """
    Performs a binomial test on a set of data.

    Args:
        df (Panda Dataframe): Data frame with metrics.
        p_value (float): Alpha value.

    Returns:
        Tuple of test result and if it is in the rejection error (i.e., more than alpha).
    """
    # get treatment data
    df = df.loc[df['control_treatment']=='treatment']

    # perform binomial test
    test_result = stats.binom_test(df['metric'].sum(), n=len(df), p=p_value, alternative='greater')

    # return test result and rejection bool
    return test_result, test_result > p_value