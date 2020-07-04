
# coding: utf-8

# # Load all the necessary libraries

# In[21]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = "ggplot2"
get_ipython().run_line_magic('matplotlib', 'inline')
data=pd.read_csv('M:\Covid19\covid_19_india.csv')


# ## Summary

# In[3]:


data.info()


# ### Attributes like mean , median , mode , count , maximum , percentage ,etc will be shown

# In[14]:


data.describe()


# ### Statewise Insights in a Tabular Fashion for better understanding

# In[15]:


# Statewise Insights
state_details = pd.pivot_table(data, values=['Confirmed','Deaths','Cured'], index='State/UnionTerritory', aggfunc='max')
# Calculating the Recovery rate statewise rounding it upto 2 decimals
# Likewise for Death Rate
state_details['Death Rate'] = round(state_details['Deaths'] /state_details['Confirmed'], 2)
#Likewise for Confirmed from highest to lowest
state_details = state_details.sort_values(by='Confirmed', ascending= False).reset_index(level=0)
# For styling
state_details.style.background_gradient(cmap='Spectral')


# ### Even better Tabular understanding to get latest number

# In[4]:


covid1=data.drop(['Sno','ConfirmedIndianNational','ConfirmedForeignNational'], axis=1)
covid1=covid1[covid1['State/UnionTerritory'] !='Cases being reassigned to states']
covid1.tail()


# ### Visualisation for Covid19 India Cured/Recovered Cases

# In[5]:


fig = px.line(covid1, x="Date", y="Cured", title='Covid19 India Cured/Recovered Cases',color='State/UnionTerritory')
fig.show()


# ### Visualisation for Covid19 India Cured/Recovered Cases in Uttar Pradesh

# In[13]:


UP=covid1[covid1['State/UnionTerritory']=='Uttar Pradesh']
fig = px.line(UP, x="Date", y="Cured", title='Cured/Recovered due to Covid19 in Uttar Pradesh')
fig.show()


# ### Visualisation for Death Cases in Uttar Pradesh due to Covid19

# In[10]:


UP=covid1[covid1['State/UnionTerritory']=='Uttar Pradesh']
fig = px.line(UP, x="Date", y="Deaths", title='Death due to Covid19 in Uttar Pradesh')
fig.show()


# ### Visualisation for Confirmed Cases in Uttar Pradesh due to Covid19

# In[12]:


UP=covid1[covid1['State/UnionTerritory']=='Uttar Pradesh']
fig = px.line(UP, x="Date", y="Confirmed", title='Confirmed Cases due to Covid19 in Uttar Pradesh')
fig.show()


# ### Density Curve

# In[9]:


# generate random normal distribution
mu, sigma = 0, 0.1 # mean and standard deviation
covid1 = np.random.normal(mu, sigma, 1000)

# plot histogram with density curve 
count, bins, ignored = plt.hist(covid1, 30, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
         np.exp( - (bins - mu)**2 / (2 * sigma**2) ), 
         linewidth=2, color='r')
plt.show()


# ### Visualisation for Confirmed Cases including Indian National and Foreign Indian National

# In[4]:


data['confirmed']=data.ConfirmedForeignNational+data.ConfirmedIndianNational


# In[22]:


grouped = data.groupby('Date')['Date', 'Confirmed', 'Deaths'].sum().reset_index()

fig = px.line(grouped, x="Date", y="Confirmed",
              title="Indiawide Confirmed Cases Over Time")
fig.show()

fig = px.line(grouped, x="Date", y="Confirmed", 
              title="Indiawide Confirmed Cases (Logarithmic Scale) Over Time", 
              log_y=True)
fig.show()


# ### Visualisation in form of Histogram

# In[39]:


data=data.rename(columns={'Date':'date',
                     'State/UnionTerritory':'state',
                         'Deaths':'deaths'})


# In[40]:


latest = data[data['date'] == max(data['date'])].reset_index()
latest_grouped = latest.groupby('state')['Confirmed', 'deaths'].sum().reset_index()


# In[44]:


latest = data[data['date'] == max(data['date'])]
latest = latest.groupby('state')['Confirmed', 'deaths'].max().reset_index()

fig = px.bar(latest.sort_values('Confirmed', ascending=False)[:15][::-1], 
             x='Confirmed', y='state', color_discrete_sequence=['#c00a56'],
             title='Confirmed Cases in India', text='Confirmed', orientation='h')
fig.show()

