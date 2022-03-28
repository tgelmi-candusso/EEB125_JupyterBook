#!/usr/bin/env python
# coding: utf-8

# # What is computation?
# 
# From [https://www.dictionary.com](https://www.dictionary.com):
# 
# * *Computation*: an act, process, or method of computing; calculation.
# * *Computing*: the use of a computer to process data or perform calculations; the act of calculating or reckoning.
# 
# In this course, a computation is a series of calculations that manipulates, analyzes, and derives information from data.

# # What's a computer?
# 
# Computation can be done by hand or it can be automated. In the 1940's, when computation became particularly important for war as technology advanced, the original modern "computers" were people.

# # Computational tools: Python and Pandas
# 
# + Python: a programming language
# + Pandas: a set of data science tools written in Python

# # Python expressions

# Python as a calculator:

# In[2]:


3 + 5


# The _type_ of these numbers is integer. In Python, we say `int`.

# In[3]:


2 + 3 / 2


# Those are called *expression*s. They can get pretty complex. Remember BEDMAS?

# In[4]:


4 / 3 + (9 - 2 * (8 + 3))


# | Precedence | Operator | Operation |
# | :- | :- | :- |
# | Highest | () | Grouping |
# |  | ** | Exponentiation |
# |  | - | Negation |
# |  | *, / //, % | Multiplication, division, integer division, remainder |
# | Lowest | +, - | Addition and substraction |

# Technically called "double-precision floating-point numbers".
# 
# Python just calls them `float`s.
# 
# You can use them just like you use real numbers, but they are very slightly inaccurate.

# In[5]:


type(2.3)


# In[6]:


type(2)


# # Naming things
# 
# Just like in math, we often want to give names to values.
# 
# Python: *assignment statement*
# 
# Assignment statement assign a value to a *variable*.

# In[7]:


x = 3 + 2


# No "Out" box!
# 
# Python only creates a box if there is a result from evaluating an expression. 
# 
# Assignment statements are not expressions, they are *statements*.
# 
# All assignment statements use the `=` symbol.
# 
# We can use `x` in later calculations.
# 
# We're going to use assignment statements to name values a *lot* in the course.

# In[8]:


x


# In[9]:


x * x


# In[10]:


x / x + x


# In[11]:


# max is a built-in function.
# This is a comment, and Python ignores it.
max(3, 4)  # What's the maximum of 3 and 4?


# In[12]:


import math
math.sqrt(x)


# Python rule: Whenever there is a division using `/`, the result is a `float`.
# 
# Python rule: Whenever a real number is involved in an expression, the result is a `float`.

# In[13]:


4.1 + 3


# In[14]:


2 ** 3


# In[15]:


x ** -1


# In[16]:


x * (x ** -1)


# ## Algorithm definition
# 
# _Algorithm_: a finite sequence of well-defined instructions ([Wikipedia](https://en.wikipedia.org/wiki/Algorithm))

# # Python's assignment statement algorithm
# 
# `var = expr`
# 
# 1. Evaluate the expression to the right of the `=`. That produces a value.
# 2. Label the produced value with the variable name.
# 
# It works right to left. The variable is not created until *after* the expression is fully evaluated.

# 
# # Algorithm: compute the average
# 
# An algorithm is a program written for humans to read and follow. The average of a list of numbers is the sum divided by the count.
# 
# 1. Sum the numbers.
# 1. Count the numbers.
# 1. Divide the sum by the count.

# What is the average of the list `1, 2, 3, 4, 5`?
# 
# 1. Sum: the sum of `1, 2, 3, 4, 5` is `15`
# 1. Count: there are `5` numbers in the list
# 1. `15 / 5` is `3`

# # Python version
# 
# We can use built-in functions `sum` and `len` to implement the algorithm in Python:

# In[17]:


numbers = [1, 2, 3, 4, 5]  # That's a list


# In[18]:


sum(numbers)


# In[19]:


type(numbers)


# In[20]:


len(numbers)


# In[21]:


total = sum(numbers)
count = len(numbers)
avg = total / count
avg


# ## Python syntax and grammar
# 
# Python has a grammar and a syntax just like human languages do
# 
# Example: lists need square brackets and commas in between items in the list.
# 
# + English essay with typos and grammatical errors? Still mostly readable.
# + Python program with typos and other errors? It can't be run.

# # Common errors
# 
# + Missing comma
# + Mismatched bracket such as `(` and `]`
# + Typo in a function or variable name
# + Incorrect calculation
# 
# You'll find lots more.  :-)

# In[22]:


sum(numbers) / 0


# # A data story
# 
# Over the next while, we'll explore the kinds of computation you'll learn how to do in this course in the context of a _data story_.

# ## Old Faithful
# 
# Old Faithful is a geyser in Yellowstone National Park in the state of Wyoming. It erupts pretty regularly, hence the name.
# 
# ![Alt Text](https://i.makeagif.com/media/3-30-2015/B6WEUM.gif)

# ## Old Faithful eruption information
# 
# Comma-separated-value (CSV) files: plain-text files that have rows of data separated by commas.
# 
# ```
# "Index", "Eruption length (mins)","Eruption wait (mins)"
#   1, 3.600, 79
#   2, 1.800, 54
#   3, 3.333, 74
#   4, 2.283, 62
#   5, 4.533, 85
# ```
# [https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html](https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html)
# 
# Research question: what's the average wait time?

# ## What programming tools do we have?
# 
# + The Python language comes with
#   - [built-in functions](https://docs.python.org/3/library/functions.html) like `sum` and `len`
#   - A large set of _modules_, which are collections of useful functions.
# + JupyterHub adds
#   - The Pandas module to Python
#   - A file system
#   - The Jupyter notebook software that interacts with Python

# 
# # `pandas`
# 
# We can read a CSV using module `pandas`.

# In[2]:


import pandas
pandas.read_csv('data//faithful.csv')


# ## Naming data
# 
# File operations are slow, and we don't want to repeat ourselves.
# 
# Read once and assign to a variable.

# In[3]:


faithful_eruptions = pandas.read_csv('data//faithful.csv')
type(faithful_eruptions.columns)


# ## What's in a name?
# 
# `faithful_eruptions` is now the name of the table of information we just read.
# 
# What's its value?
# 

# In[26]:


faithful_eruptions


# ## `DataFrame`s: manipulating and examining data
# 
# Remember how computations manipulate, analyze, and derive information from data? Here are a few things we can do with the information once we've read it.
# 
# We call that table of information a `DataFrame`. The `pandas` module has a function, `read_csv`, that opens and reads a CSV file and produces a `DataFrame`.
# 
# Much like `pandas` has data science code that we can use, like `read_csv`, `DataFrame`s have code that we can use that operate on the data inside the `DataFrame`.

# ### Examine the top few rows of a `DataFrame`
# 
# `head` is a function that produces a `DataFrame` containing o
# nly the top five rows of data.

# In[29]:


faithful_eruptions.head()


# ## Accessing a column
# 
# Sometimes we want to look at only a single column. For example, we might want to know the average wait time in minutes, and we'll want to isolate the last column. We can use the name of the column to get it:

# In[46]:


faithful_eruptions['Eruption wait (mins)']


# Let's name the column data:

# In[5]:


wait_numbers = faithful_eruptions['Eruption wait (mins)']
wait_numbers


# ## Displaying multiple values in a computation
# 
# The result of a computation is displayed below the code cell containing the computation. But what if we want to show more information?
# 
# Here, we use built-in function `print`, along with built-in functions `min` and `max`, to print both the minimum and maximum values.

# In[48]:


max_wait = max(wait_numbers)
min_wait = min(wait_numbers)
print(max_wait)
print(min_wait)


# # Using the calculate-average algorithm
# 
# Now that we have the column numbers saved in a variable, we can apply the algorithm:

# In[51]:


total = sum(wait_numbers)
count = len(wait_numbers)
avg = total / count

print("The average wait time is:")
print(avg)


# In[ ]:




