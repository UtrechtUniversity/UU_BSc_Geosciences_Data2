# Seasonality and autocorrelation


In Geoscience we often measure a variable though time. Just like in
regression

We will follow the textbook’s chapter 11.7 and use data on the trends in
atmospheric carbon dioxide from the National Oceanic and Atmospheric
Administration (NOAA, Fig. 11.9). In 1958, C.D. Keeling started
monitoring $CO_2$ levels in the Mauna Loa Observatory on Hawaii. It was
the first continuous monitoring programme and provided evidence for the
rise of $CO_2$ concentration in the atmosphere. You can find more about
it on the [curve’s official website](https://keelingcurve.ucsd.edu/).

Exercise based on [T. Haslwanter’s textbook
materials](https://github.com/thomas-haslwanter/statsintro-python-2e/blob/master/ipynbs/11_timeSeries.ipynb).

# Code

``` python
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.model import ARIMA
import statsmodels.formula.api as sm
import ssl
```

The original dataset is provided in a format that is not easy for
automatic machine reading (e.g. the column headers occupy different
number of lines). So to read it in, you would need to make it
machine-friendly, e.g. one row = one observation. We provide this
cleaned dataset for you.

Read in the dataset:

``` python
path = '../Data/monthly_in_situ_co2_mlo.csv'
df = pd.read_csv(path, sep=',')
```

Preview the dataset:

``` python
df.head()
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
&#10;    .dataframe tbody tr th {
        vertical-align: top;
    }
&#10;    .dataframe thead th {
        text-align: right;
    }
</style>

|     | Year | Month | CO2    |
|-----|------|-------|--------|
| 0   | 1958 | 3     | 315.71 |
| 1   | 1958 | 4     | 317.45 |
| 2   | 1958 | 5     | 317.51 |
| 3   | 1958 | 6     | 317.27 |
| 4   | 1958 | 7     | 315.87 |

</div>

If we wanted to plot the values in time, we could currently do it either
by month number, or by the year, but not both. You need to create an
extra variable that will represent the time in a continuous manner.

<details>
<summary>
Solution
</summary>

``` python
df['time'] = df['Year'].map(str) + '.' + df['Month'].map(str)
```

Visualize it:

``` python
df.plot('time', 'CO2')
```

![](Autocorrelation_files/figure-commonmark/cell-6-output-1.png)

Here we use the function `seasonal_decompose` from `statsmodels` to
separate the linear trend from the seasonal component. The measurements
are taken every month so the period of seasonality is 12. We use the
additive model because the amplitude of the seasonal component does not
change with the level of the time series - see eq. 11.13 in the
textbook.

### Decomposition into trend, seasonality, and residuals

``` python
result_add = seasonal_decompose(df['CO2'], 
model='additive', 
period=12, 
extrapolate_trend='freq')
```

What does the last line, `extrapolate_trend='freq'`, do? Use the
[statsmodels
documentation](https://www.statsmodels.org/dev/generated/statsmodels.tsa.seasonal.seasonal_decompose.html)
to understand all the parameters.

Now we can plot the additive components:

``` python
result_add.plot()
plt.show()
```

![](Autocorrelation_files/figure-commonmark/cell-8-output-1.png)

### Zooming in on the trend

In some applications, we might want to only understand one component of
the time series. In the case of the $CO_2$ data, the secular trend is of
wide interest and we might want to know how fast it is increasing.

Now we have to account for the fact that $CO_2$ levels in each year
depend on the value in the previous year. This is exactly why we cannot
apply regression analysis to the entire $CO_2$ variable. But we can use
the *i - 1* value to predict the *i*th value.

We use the ‘shift’ function to create a new variable that is the the
*i - 1* value of the trend.

``` python
trend = pd.DataFrame(result_add.trend)
trend['time'] = df['time']
trend['predicted'] = trend['trend'].shift(1)
```

Now we can use ordinary least squares regression to fit a model that
predicts the current trend value based on the previous one:

``` python
model_fit = sm.ols('predicted~trend', data=trend).fit()
print(model_fit.summary2())
```

                      Results: Ordinary least squares
    ===================================================================
    Model:              OLS              Adj. R-squared:     1.000     
    Dependent Variable: predicted        AIC:                -2632.0954
    Date:               2024-07-18 13:54 BIC:                -2622.7463
    No. Observations:   792              Log-Likelihood:     1318.0    
    Df Model:           1                F-statistic:        3.689e+08 
    Df Residuals:       790              Prob (F-statistic): 0.00      
    R-squared:          1.000            Scale:              0.0021043 
    ---------------------------------------------------------------------
                Coef.    Std.Err.       t        P>|t|    [0.025   0.975]
    ---------------------------------------------------------------------
    Intercept   0.3718     0.0187      19.8533   0.0000   0.3350   0.4085
    trend       0.9986     0.0001   19207.5819   0.0000   0.9985   0.9987
    -------------------------------------------------------------------
    Omnibus:              13.241        Durbin-Watson:           0.297 
    Prob(Omnibus):        0.001         Jarque-Bera (JB):        13.877
    Skew:                 -0.276        Prob(JB):                0.001 
    Kurtosis:             3.341         Condition No.:           4138  
    ===================================================================
    Notes:
    [1] Standard Errors assume that the covariance matrix of the errors
    is correctly specified.
    [2] The condition number is large, 4.14e+03. This might indicate
    that there are strong multicollinearity or other numerical
    problems.

#### Task 1

Extracts the coefficients of the model and make a plot using them. This
plot represents your model fit. Overlie on it the trend values we
calculated using decomposition, as well as the original time series. How
good is your fit?

### Seasonality

Why is the $CO_2$ level so variable during the year? And how regular is
this variability? We might want to characterise it

The first three plots are easy to interpret but what is the last one,
residuals? These are the deviations from the trend and seasonality. So
these are “anomalies” which cannot be explained by the seasonality or
the continuous trend.

``` python
%matplotlib inline

plt.plot(result_add.resid, '-')
```

![](Autocorrelation_files/figure-commonmark/cell-11-output-1.png)

We can check if there is any autocorrelation in the residuals.

``` python
plot_acf(result_add.resid)
plt.show()
```

![](Autocorrelation_files/figure-commonmark/cell-12-output-1.png)

Following the textbook, we find that: \> The systematic patterns in the
autocorrelation function show that some \> seasonal components are not
constant and have been missed. The blue \> shaded area indicates the
95%-confidence interval for the \> autocorrelation coefficients.

## Fit an ARIMA model

``` python
model = ARIMA(result_add.trend, order=(1,0,1))
model_fit = model.fit()
print(model_fit.summary())
```

    /Users/emilia/Library/Caches/pypoetry/virtualenvs/uu-bsc-geosciences-data2-8sz_r97k-py3.10/lib/python3.10/site-packages/statsmodels/tsa/statespace/sarimax.py:966: UserWarning: Non-stationary starting autoregressive parameters found. Using zeros as starting parameters.
      warn('Non-stationary starting autoregressive parameters'
    /Users/emilia/Library/Caches/pypoetry/virtualenvs/uu-bsc-geosciences-data2-8sz_r97k-py3.10/lib/python3.10/site-packages/statsmodels/tsa/statespace/sarimax.py:978: UserWarning: Non-invertible starting MA parameters found. Using zeros as starting parameters.
      warn('Non-invertible starting MA parameters found.'

                                   SARIMAX Results                                
    ==============================================================================
    Dep. Variable:                  trend   No. Observations:                  793
    Model:                 ARIMA(1, 0, 1)   Log Likelihood                 871.722
    Date:                Thu, 18 Jul 2024   AIC                          -1735.443
    Time:                        13:54:35   BIC                          -1716.740
    Sample:                             0   HQIC                         -1728.255
                                    - 793                                         
    Covariance Type:                  opg                                         
    ==============================================================================
                     coef    std err          z      P>|z|      [0.025      0.975]
    ------------------------------------------------------------------------------
    const        359.2837    668.609      0.537      0.591    -951.166    1669.734
    ar.L1          1.0000      0.000   4321.714      0.000       1.000       1.000
    ma.L1          0.9999      0.276      3.624      0.000       0.459       1.541
    sigma2         0.0063      0.001      4.571      0.000       0.004       0.009
    ===================================================================================
    Ljung-Box (L1) (Q):                  52.51   Jarque-Bera (JB):              9054.31
    Prob(Q):                              0.00   Prob(JB):                         0.00
    Heteroskedasticity (H):               4.60   Skew:                             1.42
    Prob(H) (two-sided):                  0.00   Kurtosis:                        19.31
    ===================================================================================

    Warnings:
    [1] Covariance matrix calculated using the outer product of gradients (complex-step).

``` python
model = ARIMA(result_add.resid, order=(0,0,2))
model_fit = model.fit()
print(model_fit.summary())
```

                                   SARIMAX Results                                
    ==============================================================================
    Dep. Variable:                  resid   No. Observations:                  793
    Model:                 ARIMA(0, 0, 2)   Log Likelihood                -105.285
    Date:                Thu, 18 Jul 2024   AIC                            218.571
    Time:                        13:54:36   BIC                            237.274
    Sample:                             0   HQIC                           225.759
                                    - 793                                         
    Covariance Type:                  opg                                         
    ==============================================================================
                     coef    std err          z      P>|z|      [0.025      0.975]
    ------------------------------------------------------------------------------
    const          0.0012      0.016      0.074      0.941      -0.031       0.033
    ma.L1          0.4580      0.035     12.929      0.000       0.389       0.527
    ma.L2          0.1928      0.033      5.771      0.000       0.127       0.258
    sigma2         0.0763      0.003     24.041      0.000       0.070       0.083
    ===================================================================================
    Ljung-Box (L1) (Q):                   0.03   Jarque-Bera (JB):                35.49
    Prob(Q):                              0.87   Prob(JB):                         0.00
    Heteroskedasticity (H):               1.31   Skew:                             0.17
    Prob(H) (two-sided):                  0.03   Kurtosis:                         3.98
    ===================================================================================

    Warnings:
    [1] Covariance matrix calculated using the outer product of gradients (complex-step).
