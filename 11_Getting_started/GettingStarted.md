# Getting started with data analysis

# Background to this example

Data comes in all sorts and forms within Earth sciences, from long term paleo records describing Oxygen levels in the atmosphere, timeseries of river discharge and spatio-temporal satellite images monitoring the vegetation. Within Earth Sciences we work with all these types of data to understand the past, present and future of the Earth system. Before we can work with these types of data we need to understand what we can and cannot do with the data, which conclusion we can and cannot draw.

**In this practical we will start looking at different types of data and distributions of these data to get a better understanding of the different types of data and their distributions.**

Let's start with using Python again by opening your Conda environment and then opening Spyder (for detailed instructions please look back at the first practical). We start by loading some of the stand libraries in this course. We use:

-   Pandas (data management and data handling)

-   Numpy (statistical analysis and data handling)

-   Matplotlib (plotting)

## Loading the data

``` python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
```

Now we are going to take a look at the first dataset which contains information about the amount of precipitation in the Netherlands.

``` python
precip = pd.read_csv("../Data/annualPrecipitation.csv", index_col=0)
```

In this dataset you find the annual sum of precipitation in the last century. The data is now stored in the variable *precip.* You can explore the data by looking at the data within this variable with:

``` python
precip.head()
```

Alternatively you can explore the data with the variable explorer that you find within Spyder

![By clicking on the variable you can now look at the values within the variable explorer](images/Screenshot%202024-06-21%20at%2015.45.17.png)

![](images/Screenshot%202024-06-21%20at%2015.45.41.png)

# Starting with Pandas data analysis

Next we go and look at the data by visualizing the data. Within Pandas there are multiple opportunities to explore and visualize the data. There are lots of resources to help you with using Pandas and provide nice tips, trick and examples. For example you can use a **cheat sheet** to quickly remember and double check which functions to use (e.g. <https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf>). You can also find lots of good examples that use Pandas online for different types of data and types of analysis (<https://realpython.com/search?q=pandas>).

Let's start by exploring some statistical properties of the rainfall data, starting with the mean annual precipitation.

``` python
precip.mean()
```

You can see that the Netherlands has around 800mm of precipitation per year. This amount varies year by year, and thus it can matter how many years of data you have to get the mean values. One of the important element is the amount of years of observations that are available. **We will now explore the impact of the length of the data record on the value we find for the average annual precipitation.**

Q1: Can you now make a piece of code that identifies how many year of data we have? There are two ways of exploring this, which can be using a function that checks the [length]{.underline} or the [shape]{.underline} of the Pandas array (you can use Google to help you).

If you did everything well you found that the total data record contains 118 years of data. For now we assume that the value of 800mm per year is the [true mean]{.underline} value of the annual precipitation in the Netherlands. Next we want to explore how many years of observations are needed to find the true value of annual precipitation. We will now use sub-samples of the full data record to see how many years we need. **Let's start by sub-sampling some of the data and computing and testing if the [sample mean]{.underline} accurately captures the [true mean]{.underline} (for which we now assume to be the +/- 800mm of the full data record).**

``` python
precip.sample(n = 10, replace = False, random_state=1)
```

``` python
      Precip
Year        
2000   932.4
1960   928.7
1965  1151.9
2021   861.3
1980   861.8
1952   802.1
1937   727.0
1986   716.1
1954   817.9
2003   612.7
2002   924.0
```

```{python}
precip.sample(n = 10, replace = False, random_state=1)
```

*replace = False* indicates that every year should be only selected once and no years should be sampled twice. *random_state=1* is a way of guaranteeing that the same random numbers are selected and thus the same random years (this is mostly convenient if you want to reproduce your code, like for this practical).
