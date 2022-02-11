#!/usr/bin/env python
# coding: utf-8

# # Scripting

# ### Imports

# In[4]:


import requests
from bs4 import BeautifulSoup as bs
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import getpass


# In[5]:


now = datetime.datetime.now()


# In[6]:


#Email content placeholder
content = " "


# ## Extract Hacker News

# In[7]:


def extract_news(url):
    print('Extracting Hacker News Stories')
    cnt = " "
    cnt +=('Hi,'+'<br>'+'<b>HN Top Stories:<b>\n'+'<br>'+'-'*50+'<br><br>')
    resp = requests.get(url)
    content = resp.content
    soup = bs(content,'html.parser')
    for i,tag in enumerate(soup.find_all('td',attrs={'class':'title','valign':''})):
        cnt +=((str(i+1)+' :: '+tag.text +"\n"+'<br>')if tag.text!= 'More' else "")
    return(cnt)


# In[8]:


cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ('<br>------------------------------------------<br>')
content += ('<br><br> Thank You!!')
#print(content)


# ### Sending Mail

# In[9]:


From = input('Input From mail Id -')


# In[10]:


To = input('Input To mail Id -')


# In[11]:


passw = getpass.getpass('Enter Password: ') 


# In[13]:


Server = 'smtp.gmail.com' #SMTP server 
Port  = 587 #For gmail


# In[14]:


msg = MIMEMultipart()


# In[15]:


msg['Subject'] = 'Top News Stories HN [Automated Email]'+' '+str(now.day)+'-'+str(now.month)+'-'+str(now.year)
msg['From']=From
msg['To'] = To
msg.attach(MIMEText(content,'html'))


# In[16]:


print('Initiating Server....')
server = smtplib.SMTP(Server, Port)
server.set_debuglevel(1)
server.ehlo()
server.starttls()


# In[17]:


server.login(From, passw)
server.sendmail(From, To, msg.as_string())
print('Email Sent....')
server.quit()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[1]:




