#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pydub import AudioSegment
import os


# In[2]:


cwd = os.getcwd()
cwd


# In[3]:


directory = "C:/Users/HP/Downloads/My ml project/mp3-to-wav/Argument 1/"
files = os.listdir(directory)
files


# In[4]:


x = 1
for i in files:
    song = AudioSegment.from_mp3(directory+i)
    song.export("C:/Users/HP/Downloads/My ml project/mp3-to-wav/Argument 2/"+str(x)+".wav", format="wav")
    x+=1


# In[ ]:




