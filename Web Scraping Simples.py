#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install beautifulsoup4')
import requests
import bs4


# In[2]:


url ="https://cnnespanol.cnn.com/category/inteligencia-artificial/"


# In[3]:


requisicao = requests.get(url)


# In[4]:


pagina = bs4.BeautifulSoup(requisicao.text, "html.parser")


# In[5]:


lista_noticias = pagina.find_all("a","news__media-item")
print(len(lista_noticias))


# In[6]:


for noticia in lista_noticias:
    print(noticia.get('title'))
    print(noticia.get('href'))
    print('####################################################')


# In[ ]:




