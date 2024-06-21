# Getting started with data analysis

# Background to this example

Data comes in all sorts and forms within Earth sciences, from long term paleo records describing Oxygen levels in the atmosphere, timeseries of river discharge and spatio-temporal satellite images monitoring the vegetation. Within Earth Sciences we work with all these types of data to understand the past, present and future of the Earth system. Before we can work with these types of data we need to understand what we can and cannot do with the data, which conclusion we can and cannot draw.

**In this practical we will start looking at different types of data and distributions of these data to get a better understanding of the different types of data and their distributions.**

Let's start with using Python again by opening your Conda environment and then opening Spyder (for detailed instructions please look back at the first practical). We start by loading some of the stand libraries in this course. We use:

-   Pandas (data management and data handling)

-   Numpy (statistical analysis and data handling)

-   Matplotlib (plotting)

## Code

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

