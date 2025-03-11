#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install gTTS')


# In[2]:


from gtts import gTTS


# In[3]:


convert = gTTS(text = 'I like this NLP, How about dude!', lang = "en",slow=False)
convert.save("audio.mp3")


# In[4]:


get_ipython().system('pip install pyttsx3')


# In[8]:


import pyttsx3
engine = pyttsx3.init()
engine.say("Hi, I am text to speech")
engine.runAndWait()


# In[14]:


text=['This is introduction to NLP','It is likely to useful,to people',\
      'Machine learning is the new electricity','There would be less hype around AI and more action going forward'\
      'python is the best tool!','R is good language',\
      'I want more books like this']


# In[15]:


engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()


# In[19]:


import pyttsx3
engine = pyttsx3.init()
"""RATE"""
rate=engine.getProperty('rate')
print(rate)
engine.setProperty('rate',150)
"""VOLUME"""
volume=engine.getProperty('volume')
print(volume)
engine.setProperty('volume',1.0)
"""VOICE"""
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.say("Hello World!")
engine.say('My current speaking rate is'+str(rate))
engine.say('My current speaking volume is'+str(volume))
engine.runAndWait()


# In[46]:


get_ipython().system('pip install goslate')


# In[23]:


text = "Bonjour le monde"


# In[25]:


gs = goslate.Goslate()
translatedText = gs.translate(text,'en')
print(translatedText)


# In[26]:


get_ipython().system('pip install translate')


# In[27]:


# # traslating text to telugu
from translate import Translator
translator= Translator(to_lang="te")
translation = translator.translate("How are you?")
translation


# In[28]:


# # traslating text to marathi
from translate import Translator
translator= Translator(to_lang="mr")
translation = translator.translate("How are you?")
translation


# In[30]:


# # traslating text to tamil
from translate import Translator
translator= Translator(to_lang="ta")
translation = translator.translate("How are you?")
translation


# In[31]:


from translate import Translator
translator= Translator(to_lang="hi")
translation = translator.translate("How are you?")
translation


# In[32]:


from translate import Translator
translator= Translator(to_lang="ar")
translation = translator.translate("How are you?")
translation


# In[33]:


get_ipython().system('pip install python-vlc')


# In[37]:


import vlc
p=vlc.MediaPlayer("audio.mp3")
p.play()


# In[36]:


get_ipython().system('pip install playsound')


# In[44]:


import playsound as pl
pl.playsound('audio.mp3')
print('playing sound using playsound')


# In[45]:


import speech_recognition as sr
r=sr.recognizer()
with sr.Microphone() as source:
    print("Please say something")
    audio = r.listen(source)
try:
    print("I think you said: "+r.recognize_google(audio))
except:
    pass


# In[ ]:




