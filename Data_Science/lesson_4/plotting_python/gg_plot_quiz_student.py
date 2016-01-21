import matplotlib
matplotlib.use('agg')

import pandas as pd
from ggplot import *

def lineplot(hr_year_csv):
    # Assume that we have a pandas dataframe file called hr_year, 
    # which contains two columns -- yearID, and HR.  
    # 
    # The pandas dataframe contains the number of HR hit in the
    # Major League baseball in each year.  Can you write a function,
    # lineplot, that creates a chart with points connected by lines, both
    # colored 'red', showing the number of HR by year?
    #
    # You can check out the data loaded into the dataframe at the link below:
    # https://www.dropbox.com/s/awgdal71hc1u06d/hr_year.csv
    
    # your code here
    data = pandas.read_csv(hr_year_csv)
    gg = ggplot(data,aes('yearID','HR')) + geom_point(color='red') + geom_line(color='red') + ggtitle('title') +xlab('yearID') + ylab('HR')
   
    return gg


if __name__ == "__main__":
    data = "hr_year.csv"
    image = "plot.png"
    gg =  lineplot(data)
    ggsave(image, gg, width=11, height=8)