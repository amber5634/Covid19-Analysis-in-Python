# Covid19-Analysis-in-Python
Covid19 Analysis, Prediction, Visualisation in Python

>Load the necessary Librarries

  * Pandas
  * Numpy
  * Matplotlib
  * PyPlot
  * Plotly

> For loading the library Plotly you need to install it

> For installing Plotly use the below command

```Python
pip install plotly==4.8.2
```
### Visualisation for Cured Cases in India

![Covid19 Cured Cases in India](https://user-images.githubusercontent.com/30586187/86510756-37043c00-be10-11ea-9388-6d4721b620ae.png)

### Visualisation for Cured Cases in Uttar Pradesh

![Cured Plot for Uttar Pradesh](https://user-images.githubusercontent.com/30586187/86510900-acbcd780-be11-11ea-929a-85d967081df5.png)

### Visualisatin for Death Cases due to Corona in Uttar Pradesh

![death due to Covid19 Plot in Uttar Pradesh](https://user-images.githubusercontent.com/30586187/86510904-c0683e00-be11-11ea-81d4-1334fb414d4e.png)

>For Plotting a Histogram for a density curve

```Python
# generate random normal distribution
mu, sigma = 0, 0.1 # mean and standard deviation
#name of your data set. In my case it is covid1
covid1 = np.random.normal(mu, sigma, 1000)

# plot histogram with density curve 
count, bins, ignored = plt.hist(covid1, 30, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
         np.exp( - (bins - mu)**2 / (2 * sigma**2) ), 
         linewidth=2, color='r')
plt.show()
```
### Density Curve

![DensityCurve](https://user-images.githubusercontent.com/30586187/86511065-1ee1ec00-be13-11ea-8fd0-98652d94c912.png)


### Confirmed Cases in India including Indian National and Foreign Indian National

![newplot](https://user-images.githubusercontent.com/30586187/86515419-5a41e200-be36-11ea-99df-b6d5c97a95a3.png)

### Statewise Chart

![newplot (2)](https://user-images.githubusercontent.com/30586187/86515422-5f9f2c80-be36-11ea-9280-5ad88b541686.png)

> Plotly Templates

[Click here to view Plotly Template](https://plotly.com/python/templates/)

[Kaggle dataset](https://www.kaggle.com/sudalairajkumar/covid19-in-india)

[Covid-19 India dataset Ministry of Health and Family Welfare(MoHFH) Goverment of India](https://www.mohfw.gov.in/)


> Happy Visualisation 
