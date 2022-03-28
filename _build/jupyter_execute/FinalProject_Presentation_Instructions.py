#!/usr/bin/env python
# coding: utf-8

# # EEB125H1 Data Science Conference
# 
# The final project for this course will use data science methods including programming and statistical analysis of data on  conservation risk and organismal biology.  You will present your findings in the style of an oral presentation at an academic Data Science Conference (DSC).  You and your team will give a short oral presentation of your findings, and be prepared to answer questions about your work.
# 
# ## Deliverables
# 
# 1. The Jupyter notebook (.ipynb) that produced the slides for the presentation, to be submitted before by April 6, 12:30 AM. Submission details to follow.
# 
# 2. A 5 minute oral presentation summarizing the work that you and your team will give at the Data Science Conference (DSC).
# 
# # The Data Science Conference
# 
# ## When
# 
# - __Date:__ April 6, 2022
# 
# - __Time:__ 13:00 - 15:00
# 
# ## Location 
# 
# -  UC140 (lecture room)
# 
# 
# # Conference Slides
# 
# - You should produce your conference slides using the Jupyter notebook Slideshow Extension RISE which is available on the [UofT Jupyterhub](https://jupyter.utoronto.ca). The template of a Jupyter notebook document to produce the slides for your presentation is [here](Slide_show_Instructions.ipynb).  You will be allowed to present five content slides (i.e., does not include slides to break up sections described below).
# 
# - Your presentation slides should include reproducible python output (i.e., graphs, tables should be produced by python code not hard-coded or inserted as an image), but not python code unless it's directly related to one of the sections below.  See the [template](Slide_show_Instructions.ipynb) for an example of how to write code chunks to do this.
# 
# - Your title slide must include the names of your team members, your tutorial section (e.g., TUTXXXX), and your group number as assigned by your TA.
# 
# - Your conference slides should include the following sections: 
# 
#    + Introduction 
#    + Data 
#    + Methods 
#    + Results 
#    + Conclusion  
# 
# 
# A few guidelines for an effective conference presentation:
# 
# - Your slides should be clear, concise, and easy to read quickly.
# 
# - Do not use small fonts as it will need to be read at a distance of about 6 feet.
# 
# - Figures often display information more efficiently than text.  
# 
# - Numbered or bulleted lists convey points in slides more effectively than blocks of text. 
# 
# # Oral Presentation
# 
# Your group will be asked to give a 5 minute presentation summarizing your work.  This time limit is firm and you will be asked to stop when time is up.  Each team member must speak during this presentation.
# 
# # Teamwork
# 
# - Preparatory work will be carried out in tutorials and will form part of your tutorial grade.
# 
# - You will work in a group comprised of either 3 or 4 students in the same tutorial.
# 
# - All team members are expected to contribute equally to the completion of the project.  All team members must present part of the oral presentation at the DSC.
# 
# - Your group may not work with members of another group.  You may not discuss the project with anyone except for your team, professors, and the course TAs.
# 
# - If you are concerned about any issues with your team, contact a member of the teaching team as soon as possible.
# 
# 
# # Evaluation
# 
# **Students will be evaluated as a team.**
# 
# Grade component                  |  Value 
# ---------------------------------|--------
# Content of slides                |  50%
# Reproducibility of slide content |  10%
# Oral Presentation                |  40%
# 
# 
# 
# 
# ## Reproducibility of Conference Slides
# 
# - The rubric for the content of the conference slides evaluation is below. 

# In[1]:


import pandas as pd
slidesrubric = pd.read_csv('Slide_show_Rubric.csv', keep_default_na=False)
slidesrubric.style.hide_index()


# - Before the conference presentation, you must send your TA the files to reproduce your slides by TBD.
# 
# - Your TA will attempt to reproduce your conference slides using the Jupyter notebook (.ipynb) and data files you submit.  
# 
# - If your TA cannot run the .ipynb files you submit to reproduce your conference slides content then your group will receive 0; if the TA has to make minor changes to get it to run then your group will receive 1; and if it runs with no changes then your group will receive 2. 
# 
# - If the Jupyter notebook and other files are submitted after the deadline every member of your group will lose 10% of your overall final project mark as long as they are submitted at most 24 hours after the deadline. The project files will not be accepted more than 24 hours after the deadline.
# 
# ## Oral Presentation
# 
# - Your group will give a 5 minute presentation about your work.  The rubric for the oral presentation is below.

# In[2]:


oralrubric = pd.read_csv('Presentation_Rubric.csv', keep_default_na=False)
oralrubric.style.hide_index()


# - Every member of the team is expected to speak as part of the oral presentation. One way to do this is to have each team member present at least one slide.
# 
# - If a student in a group isn’t present at their group’s presentation then they will receive 50% of the group mark.
# 
# - If a student doesn’t speak at all during the presentation and is unable to answer a direct question then they will receive 50% of the group mark. If a student neither speaks nor responds to any questions they will receive 0. 
# 
# 
# # Data Analysis Expectations
# 
# You will have the opportunity to tell your own data science story about conservation risk and organismal biology by combining evidence from several sources. Note that you do NOT have to use every possible data source in your project. However, successful projects will likely often combine at least two of the sources described below. Feel free to get in touch with one of the teaching team if you have an idea but aren't sure if it makes sufficient use of the data.
# 
# We expect that your analysis will require data wrangling, exploratory data analysis (plots and summary statistics), statistical tests and modeling.  Your project does not need to include all of these statistical methods nor does it need to include all of the variables in the data set.  You might also choose not to include all observations, or to make new variables from the data that may be more suitable for answering your questions of interest.
# 
# The goal is not to carry out an exhaustive analysis, nor to apply everything you have learned in the course.  The goal is to demonstrate that you have learned how to use python, that you can appropriately apply the methods we have covered in class to address a question, and that you can effectively interpret and present the results.
# 
# ## The Data 
# 
# We have provided data files from each of the sources explained below. The datafiles are available in the `data` directory.
# 
# ## IUCN Red List
# 
# A major focus of conservation research involves determining which geographic areas and political jurisdictions are in most need of conservation management. At the same time, many major questions in ecology and evolutionary biology surround discovering how ecological communities of organisms vary across space and time. Working in groups, you will combine several sources of data to evaluate conservation risk within an organismal group of your choice across a set of geographic regions of your choice.
# 
# To examine the conservation risks across groups of species and regions, you may use data gathered from the IUCN Red List, which we have discussed in class. In the accompanying `data/` folder, you will find two files that we have downloaded from the IUCN database-- one encompassing animal species and one encompassing plants. You can find descriptions of the data included within the columns on the IUCN website (https://www.iucnredlist.org/). You will likely want to perform your own subset of these data to extract the groups of organisms with which you are most interested.
# 
# 
# ## Amniote life history
# 
# You might also be interested in examining how extinction risk correlates to certain life history variables, similar to what we have examined in class. We will use the (creatively named) "amiote life history database" contained within `data` folder that is in the same directory as this notebook. This dataset compiles information like body size, lifespan, gestation time, across all amniotes (mammals, birds, amphibians, and reptiles). You can find metadata here:
# 
# https://figshare.com/collections/An_amniote_life-history_database_to_perform_comparative_analyses_with_birds_mammals_and_reptiles/3308127
# 
# ### Merging IUCN Red List and Amniote life history
# 
# The IUCN data (e.g., `data/IUCN_animals.csv`) has a column called `'scientificName'`, but the Amniote data (`data/Amniote_Database_Aug_2015.csv`) does not have the same column, but we can create a column in the Amniote data using `'genus'` and `'species'` columns.
# 
# The code below shows how to create this column and merge these two data sets.

# Import the csv files `IUCN_animals.csv` and `Amniote_Database_Aug_2015.csv`.  NB: these files are in the ` data` directory.

# In[3]:


import pandas as pd
animal_iucn = pd.read_csv('data/IUCN_animals.csv')
Amniote_db = pd.read_csv('data/Amniote_Database_Aug_2015.csv')


# Create a new column called `'sciname'` which concatenates `'genus'`, a blank space `' '`, and `'species'`.  

# In[4]:


sciname = Amniote_db['genus'] + ' ' + Amniote_db['species']
Amniote_db['sciname'] = sciname


# Now, we can merge `Amniote_db` (on `'sciname'`) with `animal_iucn` (on `'scientificName'`) using the `pandas` `merge` function.

# In[5]:


Amniote_iucn = Amniote_db.merge(animal_iucn, left_on='sciname', right_on='scientificName')


# ## Global Biodiversity Information Facility (GBIF)
# 
# You can use the Global Biodiversity Information Facility (GBIF) database to gather information on geographic locality (https://www.gbif.org/occurrence/search?occurrence_status=present&q=). We have provided species lists for several general geographic regions in the accompanying `data` folder. Each of these contain full lists of the species that have been documented within each region.
# 
# 
# \*(NOTE: GBIF has sort of complicated download process. If you are interested in tackling a question using a geographic region not provided, please contact Prof. Parins-Fukuchi). 
# 
# 
# 
# # Final Project Questions
# 
# Below are some general questions that your group can choose to answer in your group projects.  These general questions will require you and your group to decide which data to use to answer these questions. Your group should select one question.
# 
# 1. Some geographic regions often face differing severities of biodiversity risk, as measured by IUCN threat level. Pick two or more geographic regions and undertake a broad comparative survey of their overall risk. This will likely involve merging (by species) one or two of the provided regional species lists with one of the provided IUCN datasets (animal or plant) and then comparing the distribution of threats within each region.
# 
#   - Do your chosen regions display a difference in what kinds of organisms are most at risk? For example, are mammals more at risk in one, while flowering plants are more at risk in another? 
#   
# 2. Sometimes, geographic regions have substantially more similar biological diversity than one might expect. For example, East Asia (Japan, Korea, Taiwan, and Eastern China) has more overlap in plant species with the Appalachian mountain range in North America than one might expect given their distance. Use the GBIF data to examine the overlap in species (i.e., how many species do different regions share?) across three or more geographic regions, using the provided regional species lists. For example, using the provided GBIF data, you may compare the number of shared species or genera within North America and East Asia, and then identify whether those two regions are more similar to each other than to western Europe or eastern Africa.
# 
#   - Which regions are most similar to one another (has the greatest overlap in resident species)? Is this the set of regions that you expected to be most similar from your sample?
#   
#   - Do you notice a change in species diversity according to latitude? In other words, are regions distant from the equator more or less species rich than regions near the equator? You do not need to perform this comparison quantitatively-- just use your existing geographic knowledge to compare regions (e.g., you may already know that tropical South America is closer to the equator than northern Europe).
#   
# 3. How do biological attributes correspond to extinction risk? Do species with certain biological properties tend to be at greater risk of extinction?
#   - How does litter/clutch size (as measured in the provided 'amniote' dataset) correspond to IUCN extinction risk? Do species that birth more offspring at once have a lower risk of going extinct, on average?
#   - Are communities of animals from different regions different in their biology, on average? For example, do species in region X tend to be larger than those in region Y? To perform this comparison you may join the provided species lists with the 'amniote' dataset (merging on species) and compare the distribution of measurements for each region. For example, you may wish to ask whether North American mammals tend to be longer or shorter lived than animals in tropical South America. Try speculating on any differences you find.
