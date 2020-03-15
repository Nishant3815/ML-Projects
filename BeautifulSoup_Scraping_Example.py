#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import all the requisite libraries for extraction
import os
import re 
import wget 
import glob
import time
import selenium
import requests
import numpy as np
import pandas as pd
import zipfile as z
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request as urllib2


# In[2]:


#Header required for urllib response
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}


# In[3]:


# Enter the base website for fiercepharma
base_website =  "https://fiercepharma.com/"
# Search suffix
ssuf = "search-results/"
# Enter the keyword to search for in the entire FiercePharma website
# Note: Input for this needs to be changed in below format:
# 2 terms: Breast Cancer as "breast%20cancer"
# 3 terms: Lung Cancer Treatment as "lung%20cancer%20treatment" and so on.....
sterm = "nsclc"  
# Filter suffix
fsuf = "?filter="
# Select the type of filter to apply ("published_date" or "relevance")
filter_type = "published_date&page="                           


# In[4]:


# Initiate all possible lists
page = 1
lst_art_ttl     = []
lst_nkeywords   = []
lst_art_cat     = []
lst_auth        = []
lst_pub_date    = []
lst_art_full    = []


# In[5]:


# Main Code Block for Scraping the FiercePharma website for the given search conditions 
while(page):
    "Idea is to break the loop when it encounters a tag that has got no results message"
    temp_web = base_website+ssuf+sterm+fsuf+filter_type+str(page)
    #Check for the response from the website: If no response, try next page in except block
    try:
        response = requests.request("GET", temp_web, headers=hdr,verify=False)
    except:
        print("Error fetching a request for page: "+str(page))
        page = page+1
        continue
        
    # Fetch the html data using BeautifulSoup
    data = BeautifulSoup(response.text, 'html.parser')
    
    # In case the div tag of "results-showing-counter" doesn't exist break the loop
    if(data.find("div",{"class":"results-showing-counter"})):
        # Get all the article links present in the page 
        tag_links_list = data.select("h2 a")
        links_list     = []
        for i in tag_links_list:
            links_list.append("https://fiercepharma.com"+i.attrs["href"])
            
        # Loop through all the extracted links of the page to fetch  information    
        for index,tweb in enumerate(links_list):
            
            tweb_res  = requests.request("GET", links_list[index], headers=hdr,verify=False)
            temp_data = BeautifulSoup(tweb_res.text, 'html.parser')
            check_list_meta = []
            
            # First check if the elements are empty: if 'yes' replace by 'NA'
            
            for tag in temp_data.find_all("meta"):
                if(tag.get('name') is not None):
                    (check_list_meta.append(tag.get('name')))
                
                if(tag.get('property') is not None):
                    (check_list_meta.append(tag.get('property')))
            print(check_list_meta)
            print("***********************")
#             if('parsely-author' not in check_list_meta):
#                 print("NA")
#                 lst_auth.append('NA')
            if('parsely-pub-date' not in check_list_meta):
                lst_pub_date.append('NA')
            if('news_keywords' not in check_list_meta):
                lst_nkeywords.append('NA')
            if('og:title' not in check_list_meta):
                lst_art_ttl.append('NA')
            auth_li = []
            # Extract title and other related information
            for tag in temp_data.find_all("meta"):
                
                # Keywords extraction
                if(tag.get("name")=='news_keywords'):
                    lst_nkeywords.append(tag.get("content"))
                # Title Extraction    
                if(tag.get("property")=='og:title'):
                    lst_art_ttl.append(tag.get("content"))
                # Author Name Extraction
#                 if((tag.get("name")=='parsely-author')):
#                     print(tag.get("content"))
#                     auth_li.append(tag.get("content"))
                # Publication Date Extraction
                if(tag.get("name")=='parsely-pub-date'):
                    lst_pub_date.append(tag.get('content'))
#             lst_auth.append(auth_li)
            try:
                # Get the article associated
                if((temp_data.find('div', {'property': 'schema:articleBody'}) is None) & (temp_data.find('div', {'class': 'node__content'}) is None)):
                    lst_art_full.append('NA')
                elif (temp_data.find('div', {'property': 'schema:articleBody'})):
                    text_para = temp_data.find('div', {'property': 'schema:articleBody'})
                    lst_art_full.append(list(text_para.findChildren("p",recursive=True)))
                else:
                    text_para = temp_data.find('div', {'class': 'node__content'})
                    lst_art_full.append(list(text_para.findChildren("p",recursive=True)))
            except:
                print("Error while fetching the textual content. Check the website structure")
                # Get the associated article tag with this
            try:
                if(temp_data.find('div', {'class': 'taxonomy-term vocabulary-taxonomy'}) is None):
                    lst_art_cat.append('NA')
                    print("Hi")
                cat_li = temp_data.find('div', {'class': 'taxonomy-term vocabulary-taxonomy'})
                cl2 = str(cat_li.findChildren("h2" , recursive=True)[0])
                lst_art_cat.append(re.findall("<div>(.*?)</div>", cl2))
                print((re.findall("<div>(.*?)</div>", cl2)))
                print(page)
                print(lst_art_ttl[-1])
            except:
                print("Some error while fetching the text category from the page")
            
        page = page+1
    else:
        print("Search Complete...")
        break


# In[6]:


len(lst_art_ttl),len(lst_art_full),len(lst_art_cat),len(lst_pub_date),len(lst_nkeywords)


# In[8]:


search_df = pd.DataFrame()
search_df['Article_Title']    = lst_art_ttl
search_df['Article_Story']    = lst_art_full
# search_df['Article_Author']   = lst_auth
search_df['Article_Cat']      = lst_art_cat
search_df['Article_Pub_Date'] = lst_pub_date
search_df['Article_Keywords'] = lst_nkeywords


# In[10]:


search_df.shape


# In[11]:


search_term = 'nsclc'
filename = "fiercepharma_search_"+ search_term + "_"+ str(datetime.today().strftime('%Y_%m_%d'))+".csv"
filename


# In[12]:


search_df.to_csv(filename,index=False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




