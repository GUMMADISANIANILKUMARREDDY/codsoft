#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd 
import numpy as np 
data = { 
'A': [1, 2, np.nan, 4, 5], 
'B': [np.nan, 2, 3, 4, 5], 
'C': ['a', 'b', 'c', 'd', 'e'] 
} 
df = pd.DataFrame(data) 
print("Original DataFrame:") 
print(df) 
print("\nIdentifying missing data:") 
print(df.isnull()) 
df_dropped = df.dropna() 
print("\nDataFrame after dropping rows with missing data:") 
print(df_dropped) 
print("\nDataFrame after filling missing data:") 
numeric_columns = df.select_dtypes(include=np.number).columns 
df_filled = df.fillna(df[numeric_columns].mean()) 
print(df_filled) 
df_duplicates_removed = df.drop_duplicates() 
print("\nDataFrame after removing duplicates:") 
print(df_duplicates_removed) 


# In[4]:


import pandas as pd 
import numpy as np 
data = { 
'A': [1, 2, np.nan, 4, 5], 
'B': [np.nan, 2, 3, 4, 5], 
'C': ['a', 'b', 'c', 'd', 'e'] 
} 
print("\nModifying values using map and replace methods:") 
df_transformed = df_replace = df.replace({'A': {1: 'one', 2: 'two'}}) 
print(df_transformed) 
print("\nCreating a transformed version of the original dataset without modification:") 
df_rename = df.rename(columns={'A': 'Column_A', 'B': 'Column_B'}) 
print(df_rename) 


# In[3]:


import pandas as pd 
import numpy as np 
data = {'A': [1, 2, np.nan, 4, 5], 
'B': ['a', 'b', np.nan, 'd', 'e']} 
df = pd.DataFrame(data) 
print("\nCreating a DataFrame with normally distributed data and detecting outliers:") 
df_normal = pd.DataFrame(np.random.randn(1000, 2), columns=['A', 'B']) 
df_normal['A_outlier'] = np.abs(df_normal['A']) > 3 
df_normal['B_outlier'] = np.abs(df_normal['B']) > 3 
print(df_normal.head()) 


# In[5]:


import pandas as pd 
import numpy as np 
import re 

text = "hello\tworld this\nis a test" 
print("\nSplitting a string with a variable number of whitespace characters:") 
split_text = re.split(r'\s+', text) 
print(split_text) 
pattern = r'\w+' 
print("\nGetting a list of all patterns matching:") 
matches = re.findall(pattern, text) 
print(matches) 


# In[14]:


import pandas as pd 
index = [['A', 'A', 'B', 'B'], [1, 2, 1, 2]] 
data = [10, 20, 30, 40] 
series = pd.Series(data, index=index) 
print("Series with hierarchical indexing:") 
print(series) 
print("\nSubset at outer level:") 
print(series['A']) 
print("\nSubset at inner level:") 
print(series[:, 1])


# In[16]:


import pandas as pd 
index = [['A', 'A', 'B', 'B'], [1, 2, 1, 2]] 
data = [10, 20, 30, 40] 
series = pd.Series(data, index=index) 
index = pd.MultiIndex.from_tuples([('A', 1), ('A', 2), ('B', 1), ('B', 2)], names=['Outer', 'Inner']) 
df = pd.DataFrame({'Value': [10, 20, 30, 40]}, index=index) 
print("\nDataFrame with hierarchical indexing:") 
print(df) 
print("\nUnstacked DataFrame:") 
unstacked_df = df.unstack() 
print(unstacked_df) 
print("\nStacked DataFrame:") 
stacked_df = unstacked_df.stack() 
print(stacked_df) 


# In[19]:


import pandas as pd 
index = [['A', 'A', 'B', 'B'], [1, 2, 1, 2]] 
data = [10, 20, 30, 40] 
series = pd.Series(data, index=index) 
df1 = pd.DataFrame({'A': [1, 2, 3]}, index=[1, 2, 3]) 
df2 = pd.DataFrame({'A': [4, 5, 6]}, index=[2, 3, 4]) 
print("\nFirst DataFrame:") 
print(df1) 
print("\nSecond DataFrame:") 
print(df2) 
merged_df = pd.merge(df1, df2, left_index=True, right_index=True, suffixes=('_left', '_right')) 
print("\nMerged DataFrame using index as merge key:") 
print(merged_df) 
combined_df = df1.combine_first(df2) 
print("\nCombined DataFrame with overlap:") 
print(combined_df) 


# In[ ]:




