#!/usr/bin/env python
# coding: utf-8

# # Homework 1 — a Python intro and a data science story
# 
# ## Due Date
# 
# EEB: The homework is due 23:59 on Tuesday, January 18.
# 
# ## Purpose of Homework
# 
# Welcome to your first weekly homework assignment! You are encouraged to refer to lecture content and liberally use course resources such as the discussion board and office hours.
# 
# Homeworks build off of content explored in lecture and in lab and give you an opportunity to practice with the material. Homeworks will contain tasks that focus on tools and knowledge described in lecture and lab that week. Data science knowledge is often cumulative, and you will be asked to refer to prior weeks' content (such as loading in datasets, which is something you're going to do a lot of in this course).
# 
# Homeworks may also be continuations of the shorter labs done during that week, and will feature a relatively greater emphasis on application of tools, inquiry of concepts, and interpretation of your data science findings. Homeworks will feature a mix of coding and written response questions.
# 
# All homeworks will take place in a Jupyter notebook (like this one). When you are done, you will download this notebook and submit it to MarkUs.
# 
# ## Instructions
# 
# [Part 1](#Part-1:-Python) will teach you more about Python.  There are no questions in this part to hand in.
# 
# [Questions to Submit](#Questions-to-Submit) has questions that you will answer in a Jupyter notebook that you create.  Instructions on how to name your Jupyter notebook are in the [Creating your notebook section](#Creating-your-notebook) below.  This section contains the homework questions that you will submit via MarkUs.  The instructions for submitting to Markus are in the [Submitting your work section](#Submitting-your-work).

# # Learning objectives
# 
# By the end of this homework, you will be able to …
# 
# * apply the programming and basic data science concepts shown in lecture this week
# * answer a basic research question using Python and Pandas
# * Using JupyterHub, create a data story that demonstrates an answer to the question

# # Part 1: Python
# 
# In this part, you will learn more about Python.  But, there are no questions to hand in.
# 
# * Types
# * Expressions
# * [Built-in functions](https://docs.python.org/3/library/functions.html) Click these and read (at least) the first sentence of each description!
#   + [len](https://docs.python.org/3/library/functions.html#len)
#   + [sum](https://docs.python.org/3/library/functions.html#sum)
#   + [type](https://docs.python.org/3/library/functions.html#type)
#   + [str](https://docs.python.org/3/library/functions.html#str)
#   + [help](https://docs.python.org/3/library/functions.html#help)
# 
# 
# We will explain and explore these as we use them.

# ## Operator precedence
# 
# Just a reminder from lecture:
# 
# | Precedence | Operator | Operation |
# |:- | :- | -: |
# | Highest | () | Grouping |
# |  | ** | Exponentiation |
# |  | - | Negation |
# |  | *, / //, % | Multiplication, division, integer division, remainder |
# | Lowest | +, - | Addition and substraction |
# _Python operator precedence_

# ## Do some math in Python
# 
# 1. Click anywhere on the equation below.
# 1. Click button `Run` or type Control-Enter (or Control-Return, depending on your keyboard).
# 
# The result, `5`, will appear underneath.

# In[1]:


3 + 2


# ## Types
# 
# To Python, the `3` and the `2` are data values of type `int`. The *type* in Python dictates what Python operations we can perform on the data. 
# 
# `int` is short for _integer_, and type `int` consists of all whole numbers, both positive and negative, including `0`.
# 
# Numbers that have decimal points are of type `float`, which is short for _floating point_, which is a technical term that refers to how these numbers are stored in computer memory.
# 
# The `int`/`float` distinction is important because some operations in Python can only be done using a specific type of number (`int` or `float`). Also, the type you use will depend on the context. For example, if we were to write a program that counts the number of students enrolled in a lecture, we would use an `int` data type (we can't have half students!), and if we wanted an average we would probably want to use a `float`.

# ## Combining types using mathematical operators
# 
# Run the `Code` cell below. Notice the type of the result. The other operators (`+`, `-`, and `*`) produce integers, but `/` produces a float.

# In[2]:


3 / 2


# ## Built-in functions
# 
# Python provides a function, whose name is `type`, that returns the type of a value. Run the following Code cell to see it in action, then try various combinations of `int` and `float` values. (You can do this by changing the `3` to something like `3.14159` and re-running the cell, then changing the `2` to something with a decimal point.)

# In[3]:


type(5)


# In[4]:


type(5.1)


# ## Type `str`: strings
# 
# To use English sentences in a program we need a way to say where they start and end. Python uses either single `'` or double `"` quotes, like `'Hello world.'` and `"Hello world."`. The technical term for this kind of value is *string*, and strings contain *characters*.
# 
# Strings can be used in expressions just like `int`s and `float`s. Much like `3` is a value of type `int`, `'Hello world.'` is a value of type `str`.
# 
# Click anywhere on the string below, then click the `Run` button. (Tip: you can run the currently-selected cell by type Control-Enter.)

# In[5]:


'Hello World'


# In[6]:


type('Hello World')


# Any time you make a change to the code cell, you need to re-run that cell to see the effect. However, if our downstream cells rely on values or variables (up next!) in upstream cells, we only need to run all upstream cells once before we can run the cell in question.
# 
# The reason why Python repeats your string in the Out box is that a string is a value, and values can be used as expressions.

# ## Printing several values
# 
# Python has a built-in function named `print` that prints a value.
# 
# 

# In[7]:


print('Remember how running a Python cell displays the value of the last expression?')
print('Function `print` lets us show several results at once.')
print('Calling print with no arguments starts a new line:')
print()
print('''Let's get fancy.
This is a multi-line string.

Use triple quotes instead of single quotes.''')

name = 'Paul'  # Everything after the pound symbol is a comment. Python ignores comments.
height = 137 # cm

# More magic: you can add strings to make a longer string.
print(name + ' is ' + str(height) + ' cm tall.')

# For even more magic, tell Python to use a "format string":
# Start the whole string with the letter 'f'. How cool is that?
# Much easier for us humans to read than in the previous print statement!\n",
print(f'{name} is {height} cm tall.')


# ## Wow, that's a lot!
# 
# Yeah, you may want to spend some time making sure you understand what all that does. Ask on the course discussion board if you have questions!
# 
# Some notes:
# 
# + Python executes each line of code — each _statement_ — from top to bottom.
# + Indentation is important: so far, you can't have any spaces at the beginning of a line.
# + If the last statement is an expression, Python prints the resulting value.
# + You can't add strings and numbers together.
#   - We fix this by using built-in function `str`, which creates a string representation of its argument.

# # Questions to Submit
# 
# In lecture, we explored the average wait time between eruptions of [Old Faithful](https://en.wikipedia.org/wiki/Old_Faithful).
# 
# It's your turn to create a data story answering a data science question.

# ## Are blue jays more abundant than cardinals?
# 
# Using [blue jay data](https://raw.githubusercontent.com/tgelmi-candusso/publicrepo/main/bluejay.csv) and [cardinal data](https://raw.githubusercontent.com/tgelmi-candusso/publicrepo/main/cardinal.csv) (from the [Canadian Breeding Bird Census Plots](https://data-donnees.ec.gc.ca/data/species/assess/canadian-breeding-bird-census-plots/?lang=en)), we can answer the following question: Are blue jays or cardinals more abundant across Canada?
# 
# The two CSV files are already in JupyterHub in the same directory as this notebook.
# 
# The data includes population per hectare for each of the Census plots.
# 
# The rightmost column of each file, called `Density per 100 ha`, contains sighting information about the respective birds.

# ### Naming your notebook
# 
# Please name your notebook `EEB125_Homework_1.ipynb` so that the MarkUs autotesting can find it.

# ### Required variable names
# 
# `pandas.read_csv` returns a `DataFrame` value. You'll use it to read the `bluejay.csv` file, which is in the same folder as this notebook. Using an assignment statement, name the `DataFrame` `bluejay_df`. (Capitalization is important, MarkUs is picky.)
# 
# Do the same for `cardinal.csv`, and name that `DataFrame` `cardinal_df`.
# 
# For blue jays, in a separate Code cell, calculate the average of the column named `Density per 100 ha` and assign the returned value to variable `bluejay_avg`.
# 
# For cardinals, in a separate Code cell, calculate the average of the column named `Density per 100 ha` and assign the returned value to variable `cardinals_avg`.

# ## Notebook format to submit for homework
# 
# Use the following format in your notebook, with at least one cell (and usually several) per section. Use these titles in the Markdown so that each section is easily identifiable. Any level is fine as long as they are the same. You are welcome to add subheadings as well.
# 
# 1. **Intro:** In a Markdown cell, write a brief introduction that explains the question the notebook answers.
# 1. **Data:** This section will have both Markdown and Code cells. Give a short explanation of the format of your data, describing the columns, and use function `DataFrame.head` to show the top few lines.
# 1. **Methods:** In a sentence or two, explain how you will compute the average. (In future data stories, this section will get more complicated.)
# 1. **Computation:** You've already read in the data a previous step and named it with a variable, so do the necessary computation. Before each Code cell, provide a Markdown cell briefly explaining what the code demonstrates.
# 1. **Conclusion:** What does your evidence indicate is the answer to the question?
# 
# Remember to look at Lecture 1 for inspiration, where we implemented a very similar algorithm to compute an average from a column in a CSV file.

# ### Marking Rubric
# 
# Section                                                          | Possible grade
# -----------------------------------------------------------------|---------------------
# 1. Does the introduction explain the question in simple language?| Yes (1), No (0)
# 2. Does the data section have a Markdown cell with an explanation of the data format? |  Yes (1), No (0) 
# 3. Does the data section have a code cell where the data is read in correctly and `DataFrame.head` is used? |  Data is read correctly and `DataFrame.head` used (2), Data is read correctly, but `DataFrame.head` is not used (1), neither part is done correctly (0).
# 4. Does the computation section have a markdown cell that briefly explains what the code demonstrates? | Yes (1), No (0)
# 5. Does the computation section have a code cell that computes the correct values? | Both values are correct (2), One value is correct (1), No correct values (0)
# 6. Does the conclusion section contain a Markdown cell with an explanation of how your evidence answers the question?|Yes (1), No (0)
# Total possible mark | 8
# 
# NB: 3, 5 will be autograded.

# ## Creating your notebook
# 
# ### Step 1: create a folder for your data and notebook
# 
# + Ctrl/Cmd-click the `jupyter` icon to see your file system.
# + Make a new Folder. By default it will be called "Untitled Folder".
# ![New folder](hw1-images/JHNewFolder.png)
# __The New folder menu item__
# 

# ### Step 2: rename the file
# 
# Rename the file: click the checkbox to the left of "Untitled Folder" and click button `Rename`. Name it `EEB125_HW1`.

# ### Step 3: Upload the data to that new folder
# 
# + Double-click on the new folder to enter it.
# + Download the CSV files to your computer.
# + Now click the Upload button and upload those files.
#   - They will be placed inside the current folder.

# ### Step 4: Create your notebook
# 
# + Select `New —> Python 3 (ipython kernel)`. It will open in a new tab.
# ![New notebook](hw1-images/NewNotebook.png)
# __Fig. 1: The New Notebook menu item__
# + The notebook is named `Untitled` (in the upper left). Rename the notebook to `EEB125_Homework_1`. JupyterHub will add the `.ipynb` extension automatically in your file system.
# + The first cell is a Code cell. Change it to Markdown and type a draft of your intro. Use a title!

# ## Submitting your work
# 
# When you are ready [*], head to [MarkUs](https://markus-ds.teach.cs.toronto.edu) and submit. Upload the following:
# 
# 1. The dataset you're using.
# 1. The notebook you created.
# 
# [*] __Note: Please wait until at least Friday to try to submit to MarkUs.__

# # Rough marking rubric
# 
# + Is the data story coherent?
# + Is the writing clear?
# + Are the Markdown formatting features used effectively?
# + Does the Python code read in the data correctly? (AG)
# + Does the Python code apply the compute-the-average algorithm correctly? (AG)
# + Is the conclusion clear and correct and supported by the computation?
# 
