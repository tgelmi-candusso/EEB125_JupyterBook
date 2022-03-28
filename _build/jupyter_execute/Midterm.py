#!/usr/bin/env python
# coding: utf-8

# # EEB125 midterm
# 
# <mark> **Read this section before starting the test** </mark>
# 
# ## Test Instructions
# 
# - Complete all 5 questions below. 
# 
# - The answers to the questions will be submitted on MarkUs using a similar workflow to the lab and homework assignments, except that MarkUs will not give you feedback on passing or failing the autotests.
# 
# - Answers where you are asked to write python code will be autograded, and written answers will be graded manually by the teaching team.
# 
# 
# ## Marking Rubric
# 
# 
# Section     | 0 | 1 | 2 | 3
# ------------|---|---|---|---
# python computation steps       |auto test fails | auto test passes | NA | NA 
# Describe what you did to the data (for each part) | No answer | A partial description is given that explains what the python code did to the data| A full description that uses data science terminology is given that explains what the python code did to the data and why this step is important | NA
# Conclusion (for each part) | No answer | The question is answered but no explanation is given | The question is answered but the explanation is not supported or weakly supported by the data | The question is answered and the explanation is supported by the data 
# 
# __The total number of marks for this test is 36.__

# ## Aids Allowed and Academic Integrity
# 
# - You are allowed to use any materials from the course or any other written sources (e.g., books, websites). 
# 
# - You are not allowed to directly receive or give help during the test period.  In other words, all work must be your own, and you must not discuss or post any information about this test with anyone during the test period.
# 
# - As a student, you alone are responsible for ensuring the integrity of your work and for understanding what [constitutes an academic offense](https://www.artsci.utoronto.ca/current/academic-advising-and-support/student-academic-integrity/academic-misconduct).
# 
# ## Time Allowed
# 
# - The test will be available at 13:00 on Wednesday, February 16, and must be submitted on MarkUs (see Submission Instructions) by 15:05 PM on Wednesday, February 16.
# 
# - Late tests will receive a grade of zero unless you have an approved accommodation from your instructor.
# 
# ## How do I ask a question during the test?
# 
# - The teaching team will be available during the test on the [usual zoom class link - pw: 683207](https://utoronto.zoom.us/j/83522365155) in case you have any questions during the midterm.
# 
# - The class discussion forum  on Ed will be disabled during the test period.

# ## Submission Instructions
# 
# 1. Download this notebook using menu item `File —> Download As —> Notebook (.ipynb)`. Save it as `EEB125_Midterm.ipynb`.
# 
# 
# 2. Log in here: https://markus-ds.teach.cs.toronto.edu (Tip: Control/Command-click to open it in a new tab so you can still see these instructions.)
# 
# 
# 3. Choose your course.
# 
# 
# 4. Click the `mt: Midterm` assessment.
# 
# 
# 5. Click the `Submissions` tab. The new page is `mt: Submissions`.
# 
# 
# 6. Click button `Upload File` on the bottom right.
# 
# 
# 7. Click button `Choose Files`.
# 
# 
# 8. Select the `EEB125_Midterm.ipynb` file that you downloaded, then click Save.

# # Introduction
# 
# In this midterm, we ask you to answer the questions:
# 
# **How many kilograms of tissue do mammals grow throughout their development period?**
# 
# The code blocks and questions below will guide you through this analysis.

# # Question 1
# 
# Complete the steps below.

# ## Step 1a
# 
# We will use your student number as data for this midterm. Complete the assignment statement below by typing your student number as an `int`. __(1 mark)__

# In[1]:


'''# Answer: delete student number to create handout
stnum = '''


# In[2]:


'''# check that stnum is type int

assert type(stnum) == int'''


# ## Step 1b
# 
# Run the Code cell below to obtain your random seed for Step 3.
# 
# __NB: Be careful not to modify the Code cell.__
# 
# __(1 mark)__

# In[3]:


'''#
# CAUTION: Don't modify this code cell
#

n = len(str(stnum))
seed = int(str(stnum)[n-3:n])'''


# ## Step 2
# 
# Read the tab-separated text file `pantheria.txt` into a `pandas` `DataFrame` named `pantheria_alldat`. __(1 mark)__

# In[4]:


# put your answer in this cell


# In[5]:


'''# Check that the data makes sense
pantheria_alldat.head()'''


# ## Step 3
# 
# Run the code cell below.  This code uses `pandas.DataFrame.sample` to take a random sample of rows from `pantheria_alldat`, and name the resulting `DataFrame` `pantheria_dat`. __(1 mark)__

# In[6]:


'''#
# CAUTION: Don't modify this code cell
#

pantheria_dat = pantheria_alldat.sample(frac = 0.75, random_state = seed)'''


# In[7]:


'''# Check that you have a dataframe with the correct shape

expected_shape = (4062, 55)

error_msg = 'Go back and run the previous cells.'

assert expected_shape == pantheria_dat.shape, error_msg'''


# ## Step 4
# 
# Briefly describe what you did to the data in this question.  Put your answer in a markdown cell below. __(2 marks)__

# Step 4: Edit this Markdown cell to provide your answer:
# 

# # Question 2
# 
# ## Step 1a
# 
# A list named `important_columns` contains column names from `pantheria_dat` that will be used throughout this test is given below. Copy and paste the list below into a code cell below to define the list in python. 
# 
# ```
# important_columns = ['MSW05_Order', 
#                      'MSW05_Binomial',  
#                      '5-1_AdultBodyMass_g', 
#                      '5-3_NeonateBodyMass_g',  
#                      '23-1_SexualMaturityAge_d', 
#                      '15-1_LitterSize',
#                      '12-1_HabitatBreadth']
# 
# ```
# 
# __(1 mark)__

# In[8]:


# put your answer in this cell


# ## Step 1b
# 
# Use the list from Step 1a to select the columns in `important_columns` from `pantheria_dat`.  Name the `DataFrame` with `important_columns` `sub_pantheria`. __(1 mark)__

# In[9]:


# put your answer in this cell


# In[10]:


# Check your work
'''sub_pantheria.head()'''


# In[11]:


# check the shape of your dataframe

'''expected_shape = (4062, 7)

error_msg = 'Check that you selected the correct number of columns'

assert expected_shape == sub_pantheria.shape, error_msg'''


# ## Step 2
# 
# Create a dictionary named `columnnames` that can be used in Step 3 to rename the columns in `sub_pantheria`. Use **New column name** in the table below for the names of the new columns.  To save you time typing or cutting-and-pasting the dictionary has been partially completed in the cell below.
# 
# 
# Original column name | New column name | Description
# ---------------------|-----------------|--------------
# `'MSW05_Order'`      | `'order'`       | Taxonomic order of the species in each row
# `'MSW05_Binomial'`   | `'genus_species'`| The scientific name for each species
# `'5-1_AdultBodyMass_g '`| `'adult_mass_g'`| Average body mass of adults, measured in grams
# `'5-3_NeonateBodyMass_g'` | `'neonate_mass_g'` | Average body mass at birth, measured in grams
# `'23-1_SexualMaturityAge_d'` | `'maturity_d'` | Age at which individuals are capable of sexual reproduction, measured in days
# `'12-1_HabitatBreadth'` | `'habitat_breadth'` | Types of habitat that individuals inhabit (ground dwelling, aquatic, burrowing, and above ground dwelling)
# `'15-1_LitterSize'` | `'litter_size'` | How many offspring do mothers birth at one time?
# 

# Below is a dictionary where we have provided all the keys. Edit the dictionary to add the appropriate values. __(1 mark)__

# In[12]:


'''columnnames = {
    'MSW05_Order': ,
    'MSW05_Binomial': ,
    '5-1_AdultBodyMass_g': ,
    '5-3_NeonateBodyMass_g': ,
    '23-1_SexualMaturityAge_d': ,
    '12-1_HabitatBreadth': ,
    '15-1_LitterSize': 
}'''


# In[13]:


'''# Check your work
columnnames'''


# ## Step 3
# 
# Use `columnnames` from Step 2 to rename the columns of `sub_pantheria`, and name the new `DataFrame` `sub_pantheria_rename`. __(1 mark)__

# In[14]:


# put your answer in this cell


# In[15]:


'''# check your work

expected_colnames = ['order',
 'genus_species',
 'adult_mass_g',
 'neonate_mass_g',
 'maturity_d',
 'litter_size',
 'habitat_breadth']

assert expected_colnames == list(sub_pantheria_rename)'''


# # Step 4
# 
# Briefly describe what you did to the data in this question.  Put your answer in a markdown cell below. __(2 marks)__

# Step 4: Edit this Markdown cell to provide your answer:

# # Question 3
# 
# **Throughout this question you will see missing values such as `NaN`.  This is expected and you do not have to remove these values.**
# 
# ## Step 1
# 
# We want to answer the question: **"How many kilograms of tissue do mammals grow throughout their development period?"**
# 
# You will use columns `'adult_mass_g'`, `'neonate_mass_g'`, and `'maturity_d'` to calculate the amount of tissue, **measured in kilograms**, that individuals within each species grow, on average, throughout their development period, **in years**.  
# 
# Create the following **new** columns in `sub_pantheria_rename`.
# 
# - `'adult_mass_kg'`: defined as`'adult_mass_g'` converted to kilograms (NB: 1kg = 1000g). __(1 marks)__
# 
# - `'neonate_mass_kg'`: defined as `'neonate_mass_g'` converted to kilograms (NB: 1kg = 1000g). __(1 marks)__
# 
# - `'maturity_yrs'`: defined as `'maturity_d'` converted from days to years (NB: 1 year = 365 days). __(1 marks)__
# 

# In[16]:


# your answer goes here


# In[17]:


'''# Check your work
sub_pantheria_rename.head()'''


# ## Step 2
# 
# Use the columns that you created in Step 1 of this question: `'adult_mass_kg'`, `'neonate_mass_kg'`, and `'maturity_yrs'` to create a new column in `sub_pantheria_rename`  named `'growth_rate_kg_yr'` using the formula:
# 
# `'growth_rate_kg_yr' = ('adult_mass_kilograms' - 'neonate_mass_kilograms') / 'maturity_years'`
# 
# __(1 mark)__

# In[18]:


# your answer goes here


# In[19]:


'''# Check your work
sub_pantheria_rename.head()'''


# ## Step 3
# 
# Briefly describe what you did to the data in this question (HINT: What are the units of the column `'growth_rate_kg_yr'`?) Put your answer in a markdown cell below. __(2 marks)__ 

# Step 3: Edit this Markdown cell to provide your answer:

# # Question 4
# 
# ## Step 1
# 
# Create a new column in `sub_pantheria_rename` named `'large_litters'` that is defined as `True` if `'litter_size'` is greater than one, and `False` otherwise. __(1 mark)__

# In[20]:


# put your answer here


# In[21]:


'''# Check your work
sub_pantheria_rename.head()'''


# ## Step 2
# 
# Use the `'growth_rate_kg_yr'` column in `sub_pantheria_rename` to calculate the growth rate (kg), among mammals with `'large_litters' == True` from Step 1, such that 10% of mammals have a growth rate greater than this value (HINT: use the `quantile` function in `pandas`). 
# 
# You will do this in two stages:
# 
# - create a `DataFrame` from `sub_pantheria_rename` containing only the rows with large litters (using column `'large_litters'`, which is a Boolean `Series`), and these two columns: `'growth_rate_kg_yr'` and `'order'`. Name that new dataframe `largelit_growthrate`. __(1 mark)__

# In[22]:


# put your answer here


# In[23]:


'''# Check your work

expected_shape = (1308, 2)

error_msg = 'Check that you selected two columns'

assert expected_shape == largelit_growthrate.shape, error_msg'''


# - Now compute the value of `'growth_rate_kg_yr'` in `largelit_growthrate` such that 10% of mammals have a growth rate greater than this value (HINT: use the `quantile` function in `pandas`). Name this value `only10`. __(1 mark)__

# In[24]:


# put your answer here


# In[25]:


'''# Check your work
only10'''


# ## Step 3
# 
# Use `largelit_growthrate` from Step 2 to compute the frequency distribution of `'order'` using `value_counts`, among mammals with a `'growth_rate_kg_yr'` that is at least `only10` (from Step 2).  Name the distribution `order_dist`. 
# 
# You will do this in two stages:
# 
# - create a `DataFrame` named `large_orders` from `largelit_growthrate` that includes mammals where `'growth_rate_kg_yr'` is at least `only10` and the `DataFrame` has only the `'order'` column. __(1 mark)__
# 
# - compute the frequency distribution of `'order'` in `large_orders` and name it `order_dist`. __(1 mark)__
# 

# In[26]:


# put your answer here


# In[27]:


'''# Check your work
order_dist'''


# ## Step 4
# 
# `order_dist.index` will extract the names of the rows of `order_dist`. (Try it! Copy and paste `order_dist.index` to see its value.) Use `order_dist.index` to extract the name of the order that is most frequent, and name it `highest_order_name`. __(1 mark)__

# In[28]:


# put your answer here


# In[29]:


'''# Check your work
highest_order_name'''


# ## Step 5
# 
# Use the `pandas` functions `describe` and `groupby` to generate a quantitative summary of the distribution of `'growth_rate_kg_yr'` by `'large_litters'`. Name this `growth_largelit_dist` __(1 mark)__
# 
# NB:  `growth_largelit_dist` should only have the distributions of `'growth_rate_kg_yr'` by `'large_litters'`.

# In[30]:


# put your answer here


# In[31]:


'''# Check your work
growth_largelit_dist'''


# ## Step 6
# 
# Briefly describe what you did to the data in this question. Put your answer in a markdown cell below. __(2 marks)__ 

# Edit this cell to insert your answer to step 6.

# # Question 5
# 
# Answer the following question.
# 
# Briefly describe the relationship between litter sizes greater than one and growth rate per year by including the following in your answer.  
# 
# i) Do mammals with litter sizes greater than one grow faster than mammals with a litter size of one?  Briefly explain and provide evidence. __(3 marks)__
# 
# ii) Which mammals with litter sizes greater than one have more variation in growth rate per year than mammals with a litter size of one?  Briefly explain and provide evidence. __(3 marks)__
# 
# iii) Give a brief biological explanation that gives a rationale to your answers in i) and ii) if you haven't already done so in your explanations to i) and ii). __(3 marks)__

# Edit this cell to insert your answer.
