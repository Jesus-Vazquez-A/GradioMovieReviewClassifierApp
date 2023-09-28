#!/usr/bin/env python
# coding: utf-8

# In[22]:


import re
from bs4 import BeautifulSoup
import string
import nltk
from nltk.corpus import stopwords
from spellchecker import SpellChecker
import warnings


# In[23]:


def clean_text(text):
 
    text = re.sub(r'\\x[a-zA-Z0-9]+', '', text)
    text = re.sub(r'\\u[a-zA-Z0-9]+', '', text)
    text = re.sub(r'\\U[a-zA-Z0-9]+', '', text)
    text = re.sub(r'\\n', ' ', text)

    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    

    text = re.sub(r'[^a-zA-Z\s]', '', text)
    

    text = re.sub(r'\s+', ' ', text).strip()
    
    return text


# In[24]:


def remove_html_tags(text):
    soup = BeautifulSoup(text, 'html.parser')
    cleaned_text = soup.get_text()
    return cleaned_text





def remove_special_characters(text):

    text = text.translate(str.maketrans('', '', string.punctuation))

    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    

    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

