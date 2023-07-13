#!/usr/bin/env python
# coding: utf-8

# In[40]:


from bs4 import BeautifulSoup 
import requests


# In[41]:


url='https://suumo.jp/chintai/kyoto/ek_03650/?page={}'
target_url=url.format(1)
print(target_url)


# In[42]:


r=requests.get(target_url)
soup=BeautifulSoup(r.text)


# In[57]:


contents=soup.find_all('div',class_='cassetteitem')


# In[58]:


len(contents)


# In[59]:


content=contents[0]


# In[84]:


detail=content.find('div', class_='cassetteitem-detail')
##
table=content.find('table', class_='cassetteitem_other')


# In[85]:


title=detail.find('div' , class_='cassetteitem_content-title').text
address=detail.find('li', class_='cassetteitem_detail-col1').text
access=detail.find('li', class_='cassetteitem_detail-col2').text
age=detail.find('li', class_='cassetteitem_detail-col3').text


# In[86]:


title,address,access,age


# In[88]:


tr_tags=table.find_all('tr', class_='js-cassette_link')
tr_tag=tr_tags[0]


# In[91]:


floor,price,first_fee,capacity=tr_tag.find_all('td')[2:6]


# In[92]:


floor,price,first_fee,capacity


# In[93]:


fee,management=price.find_all('li')


# In[94]:


deposit,grutuity=first_fee.find_all('li')


# In[95]:


madori,menseki=capacity.find_all('li')


# In[100]:


d={
    'title':title,
    'address':address,
    'access':access,
    'age':age,
    'fee':fee.text,
    'management':management.text,
   'deposit':deposit.text,
    'grutuity':grutuity.text,
    'madori':madori.text,
    'manseki':menseki.text
}


# In[101]:


d


# In[102]:


d_list=[]


# In[113]:


contents=soup.find_all('div',class_='cassetteitem')

for content in contents:

   detail=content.find('div', class_='cassetteitem-detail')

   table=content.find('table', class_='cassetteitem_other')

   title=detail.find('div' , class_='cassetteitem_content-title').text
   address=detail.find('li', class_='cassetteitem_detail-col1').text
   access=detail.find('li', class_='cassetteitem_detail-col2').text
   age=detail.find('li', class_='cassetteitem_detail-col3').text

   tr_tags=table.find_all('tr', class_='js-cassette_link')

   for tr_tag in tr_tags:
    
      floor,price,first_fee,capacity=tr_tag.find_all('td')[2:6]

      fee,management=price.find_all('li')

      deposit,grutuity=first_fee.find_all('li')

      madori,menseki=capacity.find_all('li')

      d={
         'title':title,
         'address':address,
         'access':access,
         'age':age,
         'fee':fee.text,
         'management':management.text,
         'deposit':deposit.text,
         'grutuity':grutuity.text,
         'madori':madori.text,
         'manseki':menseki.text
         }

      d_list.append(d)


# In[114]:


from pprint import pprint


# In[116]:


pprint(d_list[0])
print()
pprint(d_list[1])


# In[ ]:




