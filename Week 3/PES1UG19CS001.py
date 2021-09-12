'''
Assume df is a pandas dataframe object of the dataset given
'''

import numpy as np
import pandas as pd
import random


'''Calculate the entropy of the enitre dataset'''
# input:pandas_dataframe
# output:int/float
def get_entropy_of_dataset(df):
    # TODO
    target = df[df.columns[-1]].value_counts()
    # print(target)
    entropy=0
    for i in range(len(target)):
        entropy += (-1 * target[i] * np.log2(target[i]/np.sum(target)))/np.sum(target)
    #print(entropy)
    return entropy


'''Return avg_info of the attribute provided as parameter'''
# input:pandas_dataframe,str   {i.e the column name ,ex: Temperature in the Play tennis dataset}
# output:int/float
def get_avg_info_of_attribute(df, attribute):
    # TODO
    avg_info=0
    for i in df[attribute].unique():
        temp_df = df[df[attribute]==i]
        entropy = get_entropy_of_dataset(temp_df)
        avg_info += (len(temp_df[attribute])*entropy)/len(df[attribute])
    #print(avg_info)
    return avg_info


'''Return Information Gain of the attribute provided as parameter'''
# input:pandas_dataframe,str
# output:int/float
def get_information_gain(df, attribute):
    # TODO
    information_gain=get_entropy_of_dataset(df) - get_avg_info_of_attribute(df,attribute)
    return information_gain




#input: pandas_dataframe
#output: ({dict},'str')
def get_selected_attribute(df):
    '''
    Return a tuple with the first element as a dictionary which has IG of all columns 
    and the second element as a string with the name of the column selected

    example : ({'A':0.123,'B':0.768,'C':1.23} , 'C')
    '''
    # TODO
    dic = [{}]
    for i in df.columns[:-1]:
        dic[0][i]=get_information_gain(df,i)
    val = max(dic[0].values())
    for key, value in dic[0].items():
        if val == value:
            index = key
            break
    dic.append(index)
    #print(dic)
    return tuple(dic)

# df2 = pd.read_csv('sampletest2.csv')
# print(get_selected_attribute(df2))
# print(get_selected_attribute(df2[(df2['Breathing issues'] == 'Y')]))