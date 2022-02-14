#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

get_ipython().run_line_magic('cd', '/Users/charlieovens/Desktop/v1')

df3 = pd.read_excel('withearnings.xlsx')
annual = pd.read_csv('Hp_Percentchangeyearly.csv')
LR_annaual_change = annual['Percentage change (yearly) All property types']
df4 = df3.join(LR_annaual_change)
new_annual = pd.read_csv('percentage_change_year.csv')

new_annual.rename({'Percentage change (yearly) All property types' : '% Change Price'}, axis=1, inplace=True)
LR_annaual_change = new_annual['% Change Price']
df4 = df3.join(LR_annaual_change)

df4.drop(['House Price Growth', 'SE HP Growth'], axis=1, inplace=True)

fig, ax = plt.subplots(figsize = (20,10))


ax.plot((df4['Pivotable date']), (df4['% Change Price']), color = 'y')
ax.plot((df4['Pivotable date']), (df4['Earnings Growth ']), color='r')
ax.legend(['< House Price % Change', 'Weekly Earnings % Change'])
ax.set_xlabel('Years')
ax.set_ylabel('% Change')
ax.set_xticks(['2000-01-01', '2001-01-01', '2002-01-01', '2003-01-01', '2004-01-01',
                '2005-01-01', '2006-01-01', '2007-01-01', '2008-01-01', '2009-01-01', '2010-01-01',
                '2011-01-01', '2012-01-01', '2013-01-01', '2014-01-01','2015-01-01', '2016-01-01', '2017-01-01', '2018-01-01', '2019-01-01', '2020-01-01',
                '2021-01-01'])
ax.set_xticklabels(['2000', '2001','2002', '2003', '2004', '2005', '2006', '2007','2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021'])



# In[ ]:




