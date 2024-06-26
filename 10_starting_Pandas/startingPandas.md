---
toc-title: Table of contents
---

# Starting to work with Pandas

# Background to this example

When working in Python for data analysis, the Pandas packages is one
most commonly used packages. Pandas is a fast, powerful, flexible and
easy to use open source data analysis and manipulation tool, built on
top of the Python programming language. It allows you to load,
manipulate, analyse, visualize and write data in other file formats and
ways than the original data.

**In this practical we will start exploring some of the basic functions
in Pandas, learn about the different formats and ways you can use
Pandas.**

There are lots of resources to help you with using Pandas and provide
nice tips, trick and examples. For example you can use a **cheat sheet**
to quickly remember and double check which functions to use
(e.g. <https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf>). You can also
find lots of good examples that use Pandas online for different types of
data and types of analysis (<https://realpython.com/search?q=pandas>).

Let's start with using Python again by opening your Conda environment
and then opening Spyder (for detailed instructions please look back at
the first practical). We start by loading some of the stand libraries in
this course. We use:

-   Pandas (data management and data handling)

-   Numpy (statistical analysis and data handling)

-   Matplotlib (plotting)

-   Scipy (statistical analysis)

## Code

``` python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
```

Let us first generate some random numbers to work with, for that we
sample from normal distribution with mean ($\mu$) = 0 and a standard
deviation ($\sigma$) of 1. For this we use the Numpy package and more
specifically the function
[random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html).
We will create two random datasets to play around with and explore the
potential of Pandas. For the purpose of this tutorial we also set the
[seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html)
of the random number generator. A random seed (or seed state, or just
seed) is a number (or vector) used to initialize a pseudorandom number
generator. This ensure that when we select the random numbers in for
example a exercise like this we always draw the same "random" numbers.

``` python
np.random.seed(1)
randomData_1 = np.random.normal(loc=0, scale=1, size=100)
randomData_2 = np.random.normal(loc=0, scale=1, size=100)
```

Then we put the the random data into a [Pandas
Dataframe](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)
for more easy manipulation. For this we merge the two datasets together,
labeling the first one as 'A' and the second dataset as 'B'.

``` python
df = pd.DataFrame({'A':randomData_1, 'B':randomData_2}, columns=['A','B'])
```

``` python
           A         B
0   1.624345 -0.447129
1  -0.611756  1.224508
2  -0.528172  0.403492
3  -1.072969  0.593579
4   0.865408 -1.094912
..       ...       ...
95  0.077340 -1.627438
96 -0.343854  0.602319
97  0.043597  0.420282
98 -0.620001  0.810952
99  0.698032  1.044442

[100 rows x 2 columns]
```

When you look at the Dataframe you will see a couple of typical Pandas
things, firstly you see the randomly generated numbers, you see the
column labels 'A' and 'B' and lastly you see the numbers 0 to 99
indicating the rows numbers or in this case also the index of the
dataframe. Both the
[index](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.index.html)
and the
[columns](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.columns.html)
are very important elements as they provide unique identifiers for each
individual data entry in the dataframe, a bit like coordinates on a map.
Also note that Python (and thus Pandas) by defaults start counting at 0
rather than 1 which is sometimes the case for other programming
languages.
