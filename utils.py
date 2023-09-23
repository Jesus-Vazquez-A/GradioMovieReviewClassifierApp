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
    # Eliminar emojis
    text = re.sub(r'\\x[a-zA-Z0-9]+', '', text)
    text = re.sub(r'\\u[a-zA-Z0-9]+', '', text)
    text = re.sub(r'\\U[a-zA-Z0-9]+', '', text)
    text = re.sub(r'\\n', ' ', text)
    
    # Eliminar URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    
    # Eliminar caracteres no alfabéticos y números
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Eliminar espacios en blanco adicionales
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text


# In[24]:


def remove_html_tags(text):
    soup = BeautifulSoup(text, 'html.parser')
    cleaned_text = soup.get_text()
    return cleaned_text


# In[25]:


def correct_spelling(text):
   
    spell = SpellChecker()
  
    return spell.correction(text)


# In[26]:


def remove_special_characters(text):
    # Eliminar signos de puntuación
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Eliminar otros caracteres especiales
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    
    # Eliminar espacios en blanco adicionales
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

