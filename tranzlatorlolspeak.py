#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
Translator from english to "internet cat speak". 
The goal was to translate words with spaces before and after. Words with punctuation stayed the same.

"""

# Step 1
# Import the english.txt file
og_text = open("english.txt", "r") #opening and reading original text
eng_txt = og_text.readlines()

basic_eng = ''#removing leading characters and making text lowercase 
for line in eng_txt:
    basic_eng = basic_eng + line.lstrip('')
    basic_eng = str(basic_eng.lower())


# In[2]:


# Step 2
# Import the glossary (the tranzlashun.json file)
# This dataset originally comes from the GitHub repository
# at https://github.com/irdumbs/Dumb-Cogs and is covered by an MIT license

import json
with open("tranzlashun.json", "r") as cat_tranzl:
    catspeak = json.load(cat_tranzl)


# In[3]:


# Step 3
# Translate the English text into Lolspeak
import re
replacement = lambda m: catspeak.get(m.group(), m.group())
basic_eng = re.sub("(?<=\s)\w+(?=\s)", replacement, basic_eng) #replace every word with spaces found before and after


# In[4]:


# Step 4
# Save the translated text as the "lolcat.txt" file
new_file = open('lolcat.txt', "w")
finish = new_file.write(basic_eng)
new_file.close()


# In[ ]:




