# -*- coding: utf-8 -*-
# Problem Set 5: Experimental Analysis
# Name: 
# Collaborators (discussion):
# Time:

import pylab
import re

# cities in our weather data
CITIES = [
    'BOSTON',
    'SEATTLE',
    'SAN DIEGO',
    'PHILADELPHIA',
    'PHOENIX',
    'LAS VEGAS',
    'CHARLOTTE',
    'DALLAS',
    'BALTIMORE',
    'SAN JUAN',
    'LOS ANGELES',
    'MIAMI',
    'NEW ORLEANS',
    'ALBUQUERQUE',
    'PORTLAND',
    'SAN FRANCISCO',
    'TAMPA',
    'NEW YORK',
    'DETROIT',
    'ST LOUIS',
    'CHICAGO'
]

TRAINING_INTERVAL= range(1961, 2010)
TESTING_INTERVAL = range(2010, 2016)

"""
Begin helper codeTRAINING_INTERVAL
"""
class Climate(object):
    """
    The collection of temperature records loaded from given csv file
    """
    def __init__(self, filename):
        """
        Initialize a Climate instance, which stores the temperature records
        loaded from a given csv file specified by filename.

        Args:
            filename: name of the csv file (str)
        """
        self.rawdata = {}

        f = open(filename, 'r')
        header = f.readline().strip().split(',')
        for line in f:
            items = line.strip().split(',')

            date = re.match('(\d\d\d\d)(\d\d)(\d\d)', items[header.index('DATE')])
            year = int(date.group(1))
            month = int(date.group(2))
            day = int(date.group(3))

            city = items[header.index('CITY')]
            temperature = float(items[header.index('TEMP')])
            if city not in self.rawdata:
                self.rawdata[city] = {}
            if year not in self.rawdata[city]:
                self.rawdata[city][year] = {}
            if month not in self.rawdata[city][year]:
                self.rawdata[city][year][month] = {}
            self.rawdata[city][year][month][day] = temperature
            
        f.close()

    def get_yearly_temp(self, city, year):
        """
        Get the daily temperatures for the given year and city.

        Args:
            city: city name (str)
            year: the year to get the data for (int)

        Returns:
            a 1-d pylab array of daily temperatures for the specified year and
            city
        """
        temperatures = []
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        for month in range(1, 13):
            for day in range(1, 32):
                if day in self.rawdata[city][year][month]:
                    temperatures.append(self.rawdata[city][year][month][day])
        return pylab.array(temperatures)

    def get_daily_temp(self, city, month, day, year):
        """
        Get the daily temperature for the given city and time (year + date).

        Args:
            city: city name (str)
            month: the month to get the data for (int, where January = 1,
                December = 12)
            day: the day to get the data for (int, where 1st day of month = 1)
            year: the year to get the data for (int)

        Returns:
            a float of the daily temperature for the specified time (year +
            date) and city
        """
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        assert month in self.rawdata[city][year], "provided month is not available"
        assert day in self.rawdata[city][year][month], "provided day is not available"
        return self.rawdata[city][year][month][day]

def se_over_slope(x, y, estimated, model):
    """
    For a linear regression model, calculate the ratio of the standard error of
    this fitted curve's slope to the slope. The larger the absolute value of
    this ratio is, the more likely we have the upward/downward trend in this
    fitted curve by chance.
    
    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        estimated: an 1-d pylab array of values estimated by a linear
            regression model
        model: a pylab array storing the coefficients of a linear regression
            model

    Returns:
        a float for the ratio of standard error of slope to slope
    """
    assert len(y) == len(estimated)
    assert len(x) == len(estimated)
    EE = ((estimated - y)**2).sum()
    var_x = ((x - x.mean())**2).sum()
    SE = pylab.sqrt(EE/(len(x)-2)/var_x)
    return SE/model[0]

"""
End helper code
"""

def generate_models(x, y, degs):
    """
    Generate regression models by fitting a polynomial for each degree in degs
    to points (x, y).

    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        degs: a list of degrees of the fitting polynomial

    Returns:
        a list of pylab arrays, where each array is a 1-d array of coefficients
        that minimizes the squared error of the fitting polynomial
    """
    # TODO
    cofe=[]
    for degree in degs:
        cofe.append(pylab.polyfit(x,y,degree))
    return cofe
#print(generate_models(pylab.array([1961,1962,1963]),pylab.array([-4.4,-5.5,-6.6]),[1,2]))
def r_squared(y, estimated):
    """
    Calculate the R-squared error term.
    
    Args:
        y: 1-d pylab array with length N, representing the y-coordinates of the
            N sample points
        estimated: an 1-d pylab array of values estimated by the regression
            model

    Returns:
        a float for the R-squared error term
    """
    # TODO
    se=sum((y-estimated)**(2))
    y_mean=pylab.array([((sum(y))/(len(y))) for i in range(len(y))])
    se_2=sum((y-y_mean)**(2))
    re=1-((se)/(se_2))
    return re
def evaluate_models_on_training(x, y, models):
    """
    For each regression model, compute the R-squared value for this model with the
    standard error over slope of a linear regression line (only if the model is
    linear), and plot the data along with the best fit curve.

    For the plots, you should plot data points (x,y) as blue dots and your best
    fit curve (aka model) as a red solid line. You should also label the axes
    of this figure appropriately and have a title reporting the following
    information:
        degree of your regression model,
        R-square of your model evaluated on the given data points,
        and SE/slope (if degree of this model is 1 -- see se_over_slope). 

    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        models: a list containing the regression models you want to apply to
            your data. Each model is a pylab array storing the coefficients of
            a polynomial.

    Returns:
        None
    """
    # TODO
    for m in models:
        if len(m)==2:
            estimated=pylab.array(pylab.polyval(m,x))
            pylab.scatter(x,y,c="b")
            pylab.plot(x,estimated,c="r")
            pylab.xlabel("years")
            pylab.ylabel("Celsius")
            r=r_squared(y, estimated)
            se_over_slope2=se_over_slope(x, y, estimated, m)
            pylab.title("For model with degree: "+str(len(m)-1)+" and " +"with R-square: " + str(r) + "\n" 
                        + "The data is linear so ratio of se_over_slope is "+ "\n" 
                        + str(se_over_slope2))
            pylab.show()
            pylab.pause(15)
            pylab.close()
        else:
            estimated=pylab.array(pylab.polyval(m,x))
            pylab.scatter(x,y,c="b")
            pylab.plot(x,estimated,c="r")
            pylab.xlabel("years")
            pylab.ylabel("Celsius")
            r=r_squared(y, estimated)
            pylab.title("For model with degree: "+str(len(m)-1)+" and " +"with R-square: " + str(r))
            pylab.show()
            pylab.pause(15)
            pylab.close()
    return None           
def gen_cities_avg(climate, multi_cities, years):
    """
    Compute the average annual temperature over multiple cities.

    Args:
        climate: instance of Climate
        multi_cities: the names of cities we want to average over (list of str)
        years: the range of years of the yearly averaged temperature (list of
            int)

    Returns:
        a pylab 1-d array of floats with length = len(years). Each element in
        this array corresponds to the average annual temperature over the given
        cities for a given year.
    """

    years_temps=[]
    for year in years:
        cities_mean_year=[]
        for city in multi_cities:
            city_year_temp=climate.get_yearly_temp(city,year)
            city_mean_year=pylab.mean(city_year_temp)
            cities_mean_year.append(city_mean_year)
        year_temp=sum(cities_mean_year)/len(cities_mean_year)
        years_temps.append(year_temp)
    return pylab.array(years_temps)



def moving_average(y, window_length):
    """
    Compute the moving average of y with specified window length.

    Args:
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        window_length: an integer indicating the window length for computing
            moving average

    Returns:
        an 1-d pylab array with the same length as y storing moving average of
        y-coordinates of the N sample points
    """
    m_mean=[]
    for i in range (len(y)):
        if i<(window_length-1):
            y_sum=y[0:i+1]
            mean=sum(y_sum)/len(y_sum)
            m_mean.append(mean)
        else:
            y_sum=y[i-window_length+1:i+1]
            mean_2=sum(y_sum)/len(y_sum)
            m_mean.append(mean_2)
    return pylab.array(m_mean)



def rmse(y, estimated):
    """
    Calculate the root mean square error term.

    Args:
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        estimated: an 1-d pylab array of values estimated by the regression
            model

    Returns:
        a float for the root mean square error term
    """
    # TODO
    sums=0
    for i in range(len(y)):
        sums=sums+((y[i]-estimated[i])**(2))
    return (((sums)/(len(y)))**(1/2))

def gen_std_devs(climate, multi_cities, years):
    """
    For each year in years, compute the standard deviation over the averaged yearly
    temperatures for each city in multi_cities. 

    Args:
        climate: instance of Climate
        multi_cities: the names of cities we want to use in our std dev calculation (list of str)
        years: the range of years to calculate standard deviation for (list of int)

    Returns:
        a pylab 1-d array of floats with length = len(years). Each element in
        this array corresponds to the standard deviation of the average annual 
        city temperatures for the given cities in a given year.
    """
#     TODO
    years_temps=[]
    stds=[]
    means=[]
    city_year_temp=[]
    for year in years:
        means=[]
        city_year_temp=[]
        for city in multi_cities:
            city_year_temp.append(climate.get_yearly_temp(city,year))
        
        l=len(city_year_temp[0])
        for i in range(l):
            years_temps=[]
            for X in city_year_temp:
                years_temps.append(X[i])
            mean=pylab.mean(years_temps)
            means.append(mean)
        std=pylab.std(means)
        stds.append(std)
    
    return pylab.array(stds)
      
    
    

def evaluate_models_on_testing(x, y, models):
    """
    For each regression model, compute the RMSE for this model and plot the
    test data along with the model’s estimation.

    For the plots, you should plot data points (x,y) as blue dots and your best
    fit curve (aka model) as a red solid line. You should also label the axes
    of this figure appropriately and have a title reporting the following
    information:
        degree of your regression model,
        RMSE of your model evaluated on the given data points. 

    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        models: a list containing the regression models you want to apply to
            your data. Each model is a pylab array storing the coefficients of
            a polynomial.

    Returns:
        None
    """
    # TODO
    for m in models:
            estimated=pylab.array(pylab.polyval(m,x))
            pylab.scatter(x,y,c="b")
            pylab.plot(x,estimated,c="r")
            pylab.xlabel("years")
            pylab.ylabel("Celsius")
            r=rmse(y, estimated)
            pylab.title("For model with degree: "+str(len(m)-1)+" and " +"with RMSE: " + str(r))
            pylab.show()
            pylab.pause(15)
            pylab.close()
    return None           

if __name__ == '__main__':
   
    
    # Part A.4
    i=1961
    x=[]
    y_a=[]
    y_b=[]
    data=Climate("data.csv")
    for a in range(2009-1960):
        z=i+a
        x.append(z)
    x=pylab.array(x)
    for year in x:
        y_1=data.get_daily_temp("NEW YORK", 1, 10, year)
        y_a.append(y_1)
    y_a=pylab.array(y_a)
    
    ###running regression and ploting the data
    models=generate_models(x, y_a, [1])
    evaluate_models_on_training(x, y_a, models)
    ####testing on annual data
    for year in x:
        y_1=data.get_yearly_temp("NEW YORK",year)
        y_1_m=sum(y_1)/len(y_1)
        y_b.append(y_1_m)
    y_b=pylab.array(y_b)
    ###running regression and ploting the data
    
    models=generate_models(x, y_b, [1])
    evaluate_models_on_training(x, y_b, models)
#   # Part B
    i=1961
    x=[]
    for a in range(2009-1960):
        z=i+a
        x.append(z)
    x=pylab.array(x)
    y=gen_cities_avg(data, CITIES, list(x))
    models=generate_models(x, y, [1])
    evaluate_models_on_training(x, y, models)
#     Part C
    Y=moving_average(y, 3)
    models=generate_models(x, y, [1])
    evaluate_models_on_training(x, Y, models)
    # Part D.2
    i=1961
    x=[]
    for a in range(2009-1960):
        z=i+a
        x.append(z)
    X_train=pylab.array(x)
    Y=gen_cities_avg(data, CITIES, list(X_train))
    y_train=moving_average(Y, 5)
    models=generate_models(X_train, y_train, [1,2,20])
    evaluate_models_on_training(X_train, y_train, models)
    i=2010
    x=[]
    for a in range(2015-2009):
        z=i+a
        x.append(z)
    X_test=pylab.array(x)
    Y=gen_cities_avg(data, CITIES, list(X_test))
    y_test=moving_average(Y, 5)
    evaluate_models_on_testing(X_train, y_train, models)
    evaluate_models_on_training(X_test, y_test, models)
    # Part E
    # TODO: replace this line with your code
    a=gen_std_devs(Climate("data.csv"), CITIES, TRAINING_INTERVAL)
    y_train=moving_average(a, 5)
    models=generate_models(X_train, y_train, [1])
    evaluate_models_on_training(X_train, y_train, models)
    