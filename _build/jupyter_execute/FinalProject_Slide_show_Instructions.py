#!/usr/bin/env python
# coding: utf-8

# # Some Useful Information on creating Markdown Cells and a Slideshow
# 
# <mark> **Don't include this cell as part of your presentation** </mark>
# 
# ## Markdown cells
# 
# More information about Markdown Cells in Jupyter notebooks can be found [here](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Working%20With%20Markdown%20Cells.html).
# 
# ## RISE
# 
# More information about RISE can be found [here](https://rise.readthedocs.io/en/stable/).  
# 
# A few basics to create a *basic* slideshow:
# 
# - To change a Jupyter notebook cell's Slide Type select Slideshow from the menu: View > Cell Toolbar > Slideshow
# 
# ![](rise1.png)
# 
# - Choose Slide Type as Slide 
# 
# ![](rise2.png)
# 
# - Click on the RISE icon in the toolbar to run the slideshow.
# 
# ![](rise3.png)
# 
# ## Hiding Code While Displaying Output
# 
# - You will want to display python output, but not all the code that produced the output during your presentation.  Although, we ask that your slides be reproducible, so the code and output should be in one notebook.  One way to accomplish this is to use the notebook extension called *Hide input*.  Here are the steps to trun this extension on in your notebook:
# 
# - Click on the NBextensions tab in the Jupyterhub.  You can learn more about Jupyter Notebook Extensions [here](https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/).
# 
# ![](hidecode1.png)
# 
# 
# - Then click the hide code button to hide the cell's code, but display output.
# 
# ![](hidecode2.png)
# 
# - This notebook already has this extension turned on.

# # Hiding code cell example
# 
# - The code cell below is hidden, but you should be able to see the bar plot.
# - If you select the cell below then click on the hide code cell icon again the code will become visible.

# In[11]:


import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 5, 1)

y = np.array([2, 4, 4, 1]) 


plt.bar(x = x, height = y);
plt.xlabel('x axis')
plt.ylabel('y axis');
plt.title('Plot Title');


# # Title of your group project (the title should reflect the question that you are answering)
# 
# ## Team members:  A. Pandas, B. Python, C. Health, D. Datasci  
# 
# ### Tutorial: TUTXXXX
# 
# ### Group number: XX
# 

# # Introduction
# 
# - briefly states the topic you chose and how will you approach this topic
# - provides background information needed to understand your poster
# - briefly presents the statistical approach used and maybe even one or two key figure/tables to summarize the relevant data

# # Methods
# 
# - mentions specific variables in dataset used or any data wrangling performed
# - completely and accurately describes the methods used, in paragraph form with functions and symbols in bold
# - provides enough information to allow someone to replicate your work but excludes needless detail
# 

# # Results
# 
# - presents the main findings
# - includes figures, tables, graphs if they enhance clarity of presentation of information
# - refers to the relevant self‐explanatory figures, tables, graphs in the text (e.g., See Figure 1)
# - has captions above tables but below figures and graphs (so they are self-contained)
# - does not interpret the data or draw conclusions

# # Conclusion
# 
# - briefly restates the problem you are addressing and then states the main results (in complete sentences)
# - interprets the results and summarizes how the results address the problem
# - identifies any errors found
# - discusses any challenges faced, and strengths and limitations of the project
# - offers suggestions for improvement of the project (if any)
