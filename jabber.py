#!/usr/bin/env python
# coding: utf-8

# In[7]:


#followed was done in class

def tell_me_something():
    """Wise cracking function"""
    print("Something")


# In[9]:


demo/
    jabber.py
    _init_.py
setup.py


# In[11]:


from setuptools import setup

setup(name="Demo",
     version= '0.1',
     description='A simple deomonstration package',
     url= 'https://github.com/greercr02/UVA_MOD9_InClass',
     author='Chris Greer',
     author_email='fcv7fe@virginia.edu',
     license='MIT',
     packages=['demo'])

