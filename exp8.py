#!/usr/bin/env python
# coding: utf-8

# In[12]:


import matplotlib.pyplot as plt 

# Example data 
x = [1, 2, 3, 4, 5] 
y = [1, 3, 5, 7, 9] 

# Create a line plot 
plt.plot(x, y, label='Line', color='blue') 

# Add annotation 
plt.annotate('Annotation', xy=(3, 5), xytext=(3.5, 6), 
             arrowprops=dict(facecolor='black', shrink=0.05)) 

# Set title and axis labels 
plt.title('Line Plot with Annotation') 
plt.xlabel('X-axis') 
plt.ylabel('Y-axis') 
=
"
""
# Customize ticks and labels 
plt.xticks(x) 
plt.yticks(range(0, 12, 2), [str(val) for val in range(0, 12, 2)]) 

# Add legend 
plt.legend() 

# Save the plot to a file 
plt.savefig('line_plot_with_annotation.png') 

# Show plot 
plt.show() 


# In[2]:


import pandas as pd 
import matplotlib.pyplot as plt 

# Sample DataFrame 
data = { 
    'Category': ['A', 'B', 'C', 'D'], 
    'Value1': [10, 20, 30, 40], 
    'Value2': [15, 25, 35, 45], 
    'Value3': [20, 30, 40, 50] 
} 
df = pd.DataFrame(data) 

# Plotting 
df.set_index('Category').plot(kind='bar', width=0.8, figsize=(6, 4)) 

plt.xlabel('Category') 
plt.ylabel('Value') 
plt.title('Bar plot with DataFrame data') 

# Adding legend with labels
plt.legend(title='Values', labels=['Value1', 'Value2', 'Value3'], bbox_to_anchor=(1, 1)) 

plt.xticks(rotation=0) 
plt.show()


# In[2]:


import pandas as pd 
import matplotlib.pyplot as plt 

# Sample DataFrame 
data = { 
    'Category': ['A', 'B', 'C', 'D'], 
    'Value1': [10, 20, 30, 40], 
    'Value2': [15, 25, 35, 45], 
    'Value3': [20, 30, 40, 50] 
} 
df = pd.DataFrame(data) 

# Plotting 
df.set_index('Category').plot(kind='bar', stacked=True, figsize=(6, 4)) 

plt.xlabel('Category') 
plt.ylabel('Value') 
plt.title('Stacked Bar plot with DataFrame data') 
plt.legend(title='Values', bbox_to_anchor=(1, 1)) 
plt.xticks(rotation=0) 
plt.show()


# In[13]:


import pandas as pd 
import matplotlib.pyplot as plt 
# Sample data 
data = [10, 15, 20, 25, 25, 30, 30, 30, 35, 40, 40, 40, 40, 45, 50] 
# Create histogram 
plt.figure(figsize=(6, 4)) 
plt.hist(data, bins=10, color='skyblue', edgecolor='black') 
plt.title('Histogram of Value Frequency') 
plt.xlabel('Value') 
plt.ylabel('Frequency') 
plt.grid(True) 
plt.show() 


# In[4]:


import pandas as pd 
import matplotlib.pyplot as plt 
# Sample data 
data = [10, 15, 20, 25, 25, 30, 30, 30, 35, 40, 40, 40, 40, 45, 50] 
plt.figure(figsize=(6, 4)) 
plt.hist(data, bins=10, density=True, color='skyblue', edgecolor='black', alpha=0.5) 
plt.title('Density Plot of Observed Data') 
plt.xlabel('Value') 
plt.ylabel('Density') 
# Plotting the kernel density estimate 
density = pd.Series(data).plot.kde(linewidth=2, color='red') 
plt.legend(['Kernel Density Estimate', 'Histogram']) 
plt.grid(True) 
plt.show() 


# In[16]:


import numpy as np 
import matplotlib.pyplot as plt 
# Generating random data 
x = np.random.randn(100) # Random data for the x-axis 
y = np.random.randn(100) # Random data for the y-axis 
# Create the scatter plot 
plt.figure(figsize=(6, 4)) # Set the figure size (optional) 
plt.scatter(x, y, color='blue', alpha=0.5) # Create scatter plot 
# Add title and labels 
plt.title('Scatter Plot') 
plt.xlabel('X-axis') 
plt.ylabel('Y-axis') 
# Show the plot 
plt.grid(True) # Add grid (optional) 
plt.show()


# In[17]:


import numpy as np 
import matplotlib.pyplot as plt 
# Generating random data with multiple categorical variables 
categories = ['A', 'B', 'C', 'D'] 
data = { 
'A': np.random.normal(0, 1, 100), 
'B': np.random.normal(1, 1.5, 100), 
'C': np.random.normal(2, 0.5, 100), 
'D': np.random.normal(-1, 1, 100) 
} 
# Create the box plots 
plt.figure(figsize=(6, 4)) # Set the figure size (optional) 
# Create box plots for each category 
plt.boxplot([data[cat] for cat in categories], labels=categories) 
# Add title and labels 
plt.title('Box Plot of Data with Many Categorical Variables') 
plt.xlabel('Categories') 
plt.ylabel('Values') 
# Show the plot 
plt.grid(True) # Add grid (optional) 
plt.show()


# In[ ]:





# In[ ]:




