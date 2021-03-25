#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd 
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier


# In[2]:


st.write("""
 #Basic Crop Recommendation App
 
 This app predicts the crop which can be grown based on certain criteria!

""")


# In[3]:


st.sidebar.header('User parameters')


# In[15]:


def user_input_features():
    Nitrogen_content = st.sidebar.slider('Nitrogen content',1,120, 57)
    Phosphorus_content = st.sidebar.slider('Phosphorus_content',1, 140 ,68)
    Pottasium_content = st.sidebar.slider('Pottasium_content',5, 205 , 55)
    ph = st.sidebar.slider('ph_content',4.94,6.73, 5.38)
    temperature = st.sidebar.slider('temperature',10.16 , 33.49,20.15)
    rainfall = st.sidebar.slider('rainfall',31.15, 263.96,107.26 )
    data = {'Nitrogen_content':Nitrogen_content,
            'Phosphorus_content':Phosphorus_content, 
            'Pottasium_content': Pottasium_content,
            'ph' : ph ,
            'temperature' : temperature,
            'rainfall': rainfall
              }
    features = pd.DataFrame(data , index=[0])
    return features


# In[16]:


df = user_input_features()


# In[17]:


st.subheader('user_input_parameters')
st.write(df)


# In[ ]:





# In[12]:


crop = pd.read_csv("Crop_recommendation.csv")


# In[19]:


X = crop[['N','P', 'K','temperature','ph', 'rainfall']]
Y = crop.label


# In[22]:


clf = RandomForestClassifier()
clf.fit(X,Y)


# In[23]:


prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)


# In[29]:


st.subheader('prediction')
st.write(crop.label[prediction])


# In[30]:


st.subheader('prediction probability')
st.write(prediction_proba)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




