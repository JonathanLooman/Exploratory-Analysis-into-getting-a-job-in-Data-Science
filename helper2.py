import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_dict(language_dict):
    """
    plot bar graph of dictionary with keys as the x labels and values as y values.
    """
    keys = list(language_dict.keys())
    # get values in the same order as keys, and parse percentage values
    vals = [float(language_dict[k]) for k in keys]
    plt.figure(figsize=(10,5))
    return sns.barplot(x=keys, y=vals) 



def count_languages(df1, question_dict, questionnNumber = 'Q7'):
    
    """
    Creates a dictionary of different columns and their counts.
    """
	
    internal_dict = {}
    for x in df1.columns:
        if x[0:2] == questionnNumber:
            internal_dict[question_dict[x].split(" - ")[-1]] = df1[x].count()
        
    
    return internal_dict

def percent_dictionary(df1,question_dict,  questionnNumber = 'Q7'):
    
    """
    Creates a dictionary of different columns and their percents.
    """
    internal_dict = {}
    for x in df1.columns:
        if x[0:2] == questionnNumber:
            internal_dict[question_dict[x].split(" - ")[-1]] = df1[x].count()/df1.shape[0]
        
        
    
    return internal_dict

def is_multiple(df1,questionnNumber = 'Q7'):

    """
    This method returns True if there are multiple parts to a question.
    """
    
    num_languages = 0
    for x in df1.columns:
        if x[0:2] == questionnNumber:
            num_languages+=1
    if num_languages>1:
        return True
    else:
        return False


def breakdown_main(df1,questionnNumber,question_dict, percent=True):
    
    '''Main class to call'''
    
    
    if is_multiple(df1 = df1, questionnNumber=questionnNumber ) == True:
        print('works')
        if percent ==True:
            dict1 = percent_dictionary(questionnNumber = questionnNumber, df1 = df1, question_dict=question_dict )
            plot_dict(dict1)
        elif percent==False:
            dict1 = count_languages(questionnNumber = questionnNumber, df1 = df1 ,question_dict=question_dict )
            plot_dict(dict1)
        