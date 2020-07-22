import scipy.stats as stats
import pandas as pd
import numpy as np

def numerical_mean(df):
    control_treatment_data  = [
        df['metric'].loc[df['control_treatment'] == 'control'].mean(),
            df['metric'].loc[df['control_treatment'] == 'treatment'].mean()]
    d = {'control_treatment': ['control','treatment'], 'avg': control_treatment_data}
    dataframe = pd.DataFrame(data=d)
    return dataframe


def t_test(df):
    a = df['metric'].loc[df['control_treatment'] == 'control']
    b = df['metric'].loc[df['control_treatment'] == 'treatment']
    t2, p2 = stats.ttest_ind(a,b)
    return t2, p2


def bernoulli_rate(df):
    summary = df.pivot_table(values='metric', index='control_treatment', aggfunc=np.mean)
    return summary

def binomial_test(df, p_value):
    df = df.loc[df['control_treatment']=='treatment']
    test_result = stats.binom_test(df['metric'].sum(), n=len(df), p=p_value, alternative='greater')
    return test_result, test_result > p_value