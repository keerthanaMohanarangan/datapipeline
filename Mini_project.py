#!/usr/bin/env python
# coding: utf-8

# In[195]:


import pandas as pd
import numpy as np
import argparse


# In[2]:


nfl_data = pd.read_csv('NFL Play by Play 2009-2017 (v4).csv')
sf_permits = pd.read_csv('Building_Permits.csv')


# In[3]:


nfl_data.head()


# ##Function 1 : dictionary_apply_kwarg_funs that inputs **kwargs
# The function outputs outputs from each i’th step of a data pipeline applied to a given dataset.
# 
# What this function should do : 
# 1.1 Making use of regular expressions findall command, find all steps defined by arguments of kwargs starting like “step_”. Name this variable how_many steps. This quantifies how many steps are in the data pipeline.
# 

# In[4]:


import re


# In[140]:


nfl_sub = nfl_data.loc[:,'EPA':'Away_WP_pre'].head(10)


# In[141]:


nfl_sub


# In[143]:


axis = 1
output = {}
kwargs = {'input_':nfl_sub,'step_1':pd.DataFrame.dropna, 'arg_1':{'axis':axis,'thresh':args.some_number1},
          'step_2':pd.DataFrame.dropna, 'arg_2':{'axis':1,'thresh':args.some_number2},'step_3':pd.DataFrame.dropna, 'arg_3':{'axis':1,'thresh':args.some_number3}}


# In[201]:


def main(main):
        my_parser = argparse.ArgumentParser(description='Removing Nan')
        # Add the arguments
        my_parser.add_argument('some_number1', help='small')  # y or n
        my_parser.add_argument('some_number2', help='medium')  # chammak challo
        my_parser.add_argument('some_number3', help='Large')  # values of n
        #my_parser.add_argument('--threshold', help='Threshold value. When the threshold value is methelp')  # value of k
        args = my_parser.parse_args()


# In[ ]:


intermediate = kwargs['input_']


# In[200]:


#if nfl_sub is not null:
#    output_ = dictionary_apply_kwarg_funs(**kwargs)

def dictionary_apply_kwarg_funs(**kwargs):
    '''DOCSTRING ## This will count the number of steps in pipeline and call the function for each step'''
    import re
    from operator import itemgetter
    intermediate = kwargs['input_']
    data = intermediate
    fun = re.findall(fun_string, ' ' .join(kwargs.keys()))  #This step may not be needed
    how_many_steps = re.findall('step_', ' ' .join(kwargs.keys()))
    output_ = {}
    if intermediate is not null:
        for i in len(how_many_steps+1):
            try:
                fun_string = f"step_{i}"
                stepID = fun_string
                fun_,arg_dict_ = recognize_step_i(i,**kwargs)
                print('Docstring of the function is {}'.format(recognize_step_i.__doc__[:50]))
                print('Name of the function is {}'.format(recognize_step_i.__name__))
                intermediate = fun_(**arg_dict_)
                output_[stepID] = intermediate
                return data
                return output_
            except:
                print('Program was not executed succesfully')
            
    else:
        print('Input Data is Empty')
        
    #finally:
               
     #   print(T'his is finally block')
            
    


# In[192]:


#intermediate = kwargs['input_']


# In[202]:


def recognize_step_i(i, **kwargs):
    ''' ## DOCSTRING- This will return function and arguments of each step to the calling function'''
    import re
    from operator import itemgetter
    #for i in range(1, len(how_many_steps)):
    for i in range(1,4):
        
        fun_string = f"step_{i}"
        arg_string = f"arg_{i}"
        #key = re.findall(fun_string, ' ' .join(kwargs.keys()))
        #key_arg = re.findall(arg_string, ' ' .join(kwargs.keys()))

        #print(kwargs[key])  # Another method
        
        fun1 = itemgetter(fun_string)(kwargs)        
        arg_dict = itemgetter(arg_string)(kwargs)
        return arg_dict
        return fun1
        
       
    
    


#  1.2   Get the input dataset that is passed to the data pipeline (assume that it is passed to kwargs as “input_”). 
# Also create a dictionary to store the output values from the data pipeline application, call the dictionary “output_

# 1.6.3 Get the function itself by applying itemgetter to the function over the kwargs.

# In[ ]:




